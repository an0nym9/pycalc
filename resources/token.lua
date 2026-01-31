local Token = {}
Token.__index = Token

function Token:new(type, value)
    local instance = {}
    setmetatable(instance, Token)
    instance.type = type or "Unknown"
    instance.value = value or "Unknown"
    return instance
end

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

local function handle_identifiers(i, str)
    local start = i

    while i <= #str and str:sub(i, i):match("[%w_]") do
        i = i + 1
    end

    return Token:new("identifier", str:sub(start, i - 1)), i
end

local function handle_operators(i, str)
    return Token:new("operator", str:sub(i, i)), i + 1
end

local function handle_parentheses(i, str)
    return Token:new("paren", str:sub(i, i)), i + 1
end

local function handle_comma(i, str)
    return Token:new("comma", ","), i + 1
end

local function handle_whitespace(i, str)
    while i <= #str and str:sub(i, i):match("%s") do
        i = i + 1
    end
    return nil, i
end

local function tokenize(str)
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
        elseif c:match("[%+%-%*/%^]") then
            token, i = handle_operators(i, str)
        elseif c:match("[%(%)]") then
            token, i = handle_parentheses(i, str)
        elseif c == "," then
            token, i = handle_comma(i, str)
        elseif c:match("%s") then
            token, i = handle_whitespace(i, str)
        else
            error("Unknown character: " .. c)
        end

        if token then
            table.insert(tokens, token)
        end
    end

    return tokens
end
