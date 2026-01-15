-- br-to-linebreak.lua
-- Обрабатывает <br>, <br/>, <br /> в любом месте, в том числе слитно

function Inline (el)
  if el.t == "RawInline" and el.format == "html" then
    -- Ловим любой <br...> даже без пробелов
    if el.text:match("<br%s*/?>") or el.text:match("<br%s*>") then
      return pandoc.LineBreak()
    end
  end
  return el
end

-- На случай, если <br> попал внутрь Str (редко, но бывает)
function Str (str)
  local new_inlines = {}
  local text = str.text
  local i = 1
  while i <= #text do
    local pos = text:find("<br", i)
    if pos then
      if pos > i then
        table.insert(new_inlines, pandoc.Str(text:sub(i, pos-1)))
      end
      table.insert(new_inlines, pandoc.LineBreak())
      -- Пропускаем тег
      local end_pos = text:find(">", pos)
      i = end_pos and end_pos + 1 or #text + 1
    else
      table.insert(new_inlines, pandoc.Str(text:sub(i)))
      break
    end
  end
  return new_inlines
end