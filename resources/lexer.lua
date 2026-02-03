--@class Token
--@field type string
--@field value string
local Token = {}
Token.__index = Token

--@param type string
--@param type string
--@return Token
function Token:new(type, value)
    local instance = {}
    setmetatable(instance, Token)
    instance.type = type or "Unknown"
    instance.value = value or "Unknown"
    return instance
end

-- get all the numbers with the given substring
--@param i number
--@param str string
--@return Token
local function handle_numbers(i, str)
    local start = i
    local hasDot = false
    while i <= #str do
        local c = str:sub(i, i)
        if c == "." then
            if hasDot then break end
            hasDot = true
        elseif not c:match("%d") then
            break
        end
        i = i + 1
    end
    return Token:new("number", str:sub(start, i - 1)), i
end

-- get all the identifiers with the given substring
--@param i number
--@param str string
--@return Token
local function handle_identifiers(i, str)
    local start = i
    while i <= #str and str:sub(i, i):match("[%w_]") do
        i = i + 1
    end
    return Token:new("identifier", str:sub(start, i - 1)), i
end

-- ignore whitespaces of the given substring and return the new index position
--@param i number
--@param str string
--@return nil, i
local function handle_whitespace(i, str)
    while i <= #str and str:sub(i, i):match("%s") do
        i = i + 1
    end
    return i
end

-- tokenize the following expression
--@param str string
--@return table
function lexer(str)
    str = tostring(str)
    local tokens = {}
    local i = 1
    while i <= #str do
        local c = str:sub(i, i)
        local token
        if c:match("%d") then
            token, i = handle_numbers(i, str)
        elseif c:match("[%a_]") then
            token, i = handle_identifiers(i, str)
        elseif c:match("[%+%-%*/%^%=]") then
            token, i = Token:new("operator", str:sub(i, i)), i + 1
        elseif c:match("[%(%)]") then
            token, i = Token:new("paren", str:sub(i, i)), i + 1
        elseif c == "," then
            token, i = Token:new("comma", ","), i + 1
        elseif c:match("%s") then
            token, i = nil, handle_whitespace(i, str)
        else
            error("Unknown character: " .. c)
        end
        if token then
            table.insert(tokens, token)
        end
    end
    return tokens
end
