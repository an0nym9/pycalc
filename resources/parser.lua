-- check if an element is in a seqeunce
local function is_found(target, table)
    local found = false
    for _, key in ipairs(table) do
        if key == target then
            found = true
            break
        end
    end
    return found
end

-- validate tokens
function validate(tokens)
    local prevType = nil
    for _, token in ipairs(tokens) do
        if prevType == token.type then
            error("Invalid syntax")
        end
        if token.type == "identifier" then
            if token.value == "pi" then
                token.type = "number"
                token.value = math.pi
            end
        end
        prevType = token.type
    end
    return tokens
end

-- rebuilding the expression so it will be easier to compute
function parser(tokens)
    local expr = ""
    local prevType = nil
    for _, token in ipairs(tokens) do
        if prevType == "number" and not is_found(
                token.type, { "operator", "paren", "comma" }
            ) then
            expr = expr .. "*" .. token.value
        else
            expr = expr .. token.value
        end
        prevType = token.type
    end
    return expr
end
