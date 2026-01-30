-- Preprocess input before passing it into python
function preprocess(expr)
    expr = tostring(expr or "")
    expr = expr:gsub("(%d*)pi", function(n)
        if n == "" then return tostring(math.pi) else return n .. " * " .. tostring(math.pi) end
    end)
    expr = expr:gsub("%^", " ** ")
    expr = expr:gsub("pi", tostring(math.pi))
    return expr
end
