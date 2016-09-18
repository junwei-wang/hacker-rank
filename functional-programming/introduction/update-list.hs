f arr = map abs arr

main = do
  input <- getContents
  mapM_ putStrLn $ map show $ f $ map (read :: String -> Int) $ lines input
