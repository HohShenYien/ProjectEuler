-- bruteforce method

isPal :: Int -> Bool

isPal num   | (show num) == reverse' num = True
            | otherwise = False
            where reverse' num = reverse (show num)

max' :: [Int] -> Int

max' [x] = x
max' (x:xs) = max x (max' xs)

largest = max' (filter isPal [x * y | x <- [999, 998..100], y <- [999, 998..100]])

-- smarter way, knowing that one of the numbers is multiple of 11

largest' = max' (filter isPal [x * y | x <- (filter (\x -> x `mod` 11 == 0) [999, 998..100]), y <- [999, 998..100]])
