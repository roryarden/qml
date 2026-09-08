-- Clean up artifacts left over when converting arXiv LaTeXML HTML to Markdown.

local function is_blank(el)
  return pandoc.utils.stringify(el):gsub("%s", "") == ""
end

-- arXiv emits empty / bare "mailto:" hrefs for author emails; keep the visible
-- text and drop the dead link.
function Link(el)
  if el.target == "" or el.target == "mailto:" then
    return el.content
  end
  -- Drop the ltx_ref class/id so GFM can emit [text](target) instead of raw HTML.
  el.attr = pandoc.Attr()
  return el
end

-- Gather every row of a table across its head, bodies, and foot.
local function all_rows(el)
  local rows = {}
  for _, r in ipairs(el.head.rows) do
    table.insert(rows, r)
  end
  for _, body in ipairs(el.bodies) do
    for _, r in ipairs(body.head) do
      table.insert(rows, r)
    end
    for _, r in ipairs(body.body) do
      table.insert(rows, r)
    end
  end
  for _, r in ipairs(el.foot.rows) do
    table.insert(rows, r)
  end
  return rows
end

-- Layout tables (author block) convert to empty pipe-table stubs; equation
-- floats convert to fenced math trapped inside a table cell (invalid GFM).
function Table(el)
  if is_blank(el) then
    return {}
  end

  -- Detect equation-layout tables: math present, no prose words.
  local words, has_math = 0, false
  pandoc.walk_block(el, {
    Str = function(s)
      if s.text:match("%a") then
        words = words + 1
      end
    end,
    Math = function()
      has_math = true
    end,
  })
  if not has_math or words > 0 then
    return nil
  end

  -- Join the math cells within each row into a single display equation so
  -- aligned multi-line equations stay on one line each.
  local blocks = {}
  for _, row in ipairs(all_rows(el)) do
    local parts = {}
    for _, cell in ipairs(row.cells) do
      pandoc.walk_block(pandoc.Div(cell.contents), {
        Math = function(m)
          table.insert(parts, m.text)
        end,
      })
    end
    if #parts > 0 then
      local tex = table.concat(parts, " ")
      table.insert(blocks, pandoc.Para({ pandoc.Math("DisplayMath", tex) }))
    end
  end
  return blocks
end

-- LaTeXML footnote-marker leakage that survives as literal text.
function Str(el)
  if el.text == "footnotemark" or el.text == "footnotemark:" then
    return {}
  end
end

-- Expand Dirac-notation / bold-math macros that GitHub's KaTeX cannot render.
-- %b{} matches a balanced {..} group; braces are kept so a command like
-- \langle cannot merge with the following letter.
function Math(el)
  local t = el.text
  -- \displaystyle is redundant in a display block and doubles up when we join
  -- aligned equation rows, which can trip up GitHub's KaTeX.
  t = t:gsub("\\displaystyle%s*", "")
  t = t:gsub("\\ketbra%s*(%b{})%s*(%b{})", "\\lvert%1\\rangle\\langle%2\\rvert")
  t = t:gsub("\\braket%s*(%b{})%s*(%b{})", "\\langle%1\\vert%2\\rangle")
  t = t:gsub("\\ket%s*(%b{})", "\\lvert%1\\rangle")
  t = t:gsub("\\bra%s*(%b{})", "\\langle%1\\rvert")
  t = t:gsub("\\bm%s*(%b{})", "\\boldsymbol%1")
  el.text = t
  return el
end
