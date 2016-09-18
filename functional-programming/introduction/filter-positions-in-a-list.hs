f :: [Int] -> [Int]
f [] = []
f [x] = []
f (_:x:xs) = x : (f xs)

main :: IO()
main = do
  inputdata <- getContents
  mapM_ (putStrLn. show). f. map read. lines $ inputdata
