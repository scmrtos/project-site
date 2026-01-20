function Pandoc(doc)
  local new_blocks = {}
  local i = 1
  
  while i <= #doc.blocks do
    local block = doc.blocks[i]
    
    -- Ищем pymdownx.blocks.caption: /// Caption ///
    if block.tag == "Para" and pandoc.utils.stringify(block):match("^///") then
      local caption_text = pandoc.utils.stringify(block):gsub("^///%s*Caption%s*\n?(.-)%s*///%s*$", "%1")

      if caption_text ~= "" then
        -- bold, centering, not break from described object
        local caption_latex = string.format([[
\noindent
{\centering\bfseries\sffamily\small %s\par}
]], caption_text)
        
        table.insert(new_blocks, pandoc.RawBlock("latex", caption_latex))
      end
      
      -- skip ending /// block
      i = i + 1
    else
      table.insert(new_blocks, block)
      i = i + 1
    end
  end
  
  doc.blocks = new_blocks
  return doc
end
