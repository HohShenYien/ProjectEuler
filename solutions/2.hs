helper:: Int -> Int -> Int -> Int

helper num1 num2 total_so_far   | (fromIntegral num1) > 6000000 = total_so_far
                                | otherwise = let num3 = num2 + num1 in
                                                if num1 `mod` 2 == 0
                                                    then let new_total = total_so_far + num1 in
                                                    helper num2 num3 new_total
                                                else helper num2 num3 total_so_far

res = helper 1 2 0
