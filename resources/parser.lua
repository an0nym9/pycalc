-- check if an element is in a seqeunce
--@param target string
--@param table table
--@return boolean
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
--@param tokens table
--@return table
function validate(tokens)
    local prev_type = nil
    for _, token in ipairs(tokens) do
        if prev_type == token.type then
            error("Invalid syntax")
        end
        if token.type == "identifier" then
            if token.value == "pi" then
                token.type = "number"
                token.value = math.pi
            end
        end
        prev_type = token.type
    end
    return tokens
end

-- rebuilding the expression so it will be easier to compute
--@param tokens table
--@return table
function parser(tokens)
    local expr = ""
    local prev_type = nil
    for _, token in ipairs(tokens) do
        if prev_type == "number" and not is_found(
                token.type, { "operator", "paren", "comma" }
            ) then
            expr = expr .. "*" .. token.value
        else
            expr = expr .. token.value
        end
        prev_type = token.type
    end
    return expr
end
