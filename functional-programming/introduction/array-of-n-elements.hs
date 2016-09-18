fn n = take n (repeat n)

main :: IO()
main = do
  n <- readLn :: IO Int
  print $ fn n
