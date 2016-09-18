len :: [a] -> Int
len [] = 0
len (_:xs) = 1 + len(xs)

main = do
  inputdata <- getContents
  print $ len $ map (read :: String -> Int) $ lines inputdata
