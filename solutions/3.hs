firstPrime::[Int]->Int

firstPrime ls = let x = head ls in
                        if x `mod` 2 /= 0 && all (\y -> x `mod` y /= 0) [3, 5..(floor (sqrt (fromIntegral x)))]
                            then x
                        else firstPrime (tail ls)

find::Int -> Int

find num = let factors = [x | x <- [root + 1, root..2], num `mod` x == 0] in
            firstPrime factors
            where root = floor (sqrt (fromIntegral num))

res = find 600851475143
