base x 0 = 1
base x 1 = x
base x n = x / n * (base x (n-1))

solve :: Double -> Double
solve x = fromInteger (round $ sum (map (base x) [0..9]) * 10000) / 10000

main :: IO()
main = do
  getContents >>= mapM_ print. map solve. map (read :: String -> Double). tail. words
