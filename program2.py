def decode_message(message: str, pattern: str) -> bool:
    m, p = len(message), len(pattern)
    
    # dp[i][j] will be True if pattern[:j] matches message[:i]
    dp = [[False] * (p + 1) for _ in range(m + 1)]

    # Base case: empty pattern matches empty message
    dp[0][0] = True

    # Handle patterns with leading '*', which can match an empty message
    for j in range(1, p + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, p + 1):
            if pattern[j - 1] == '?' or pattern[j - 1] == message[i - 1]:
                # If the current characters match or pattern has '?'
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                # '*' can either match zero characters (dp[i][j-1]) or
                # match one character (dp[i-1][j])
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    # The result is whether the entire message matches the entire pattern
    return dp[m][p]
