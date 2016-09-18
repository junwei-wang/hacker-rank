f :: Int -> [Int] -> [Int]
f n arr = filter (<n) arr

main = do
  n <- readLn :: IO Int
  inputData <- getContents
  let numbers = map read (lines inputData) :: [Int]
  putStrLn . unlines $ (map show . f n) numbers
