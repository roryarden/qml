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

-- Layout tables (e.g. the author block) can convert to empty pipe-table stubs.
function Table(el)
  if is_blank(el) then
    return {}
  end
end

-- LaTeXML footnote-marker leakage that survives as literal text.
function Str(el)
  if el.text == "footnotemark" or el.text == "footnotemark:" then
    return {}
  end
end
