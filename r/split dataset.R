# splitting a dataset to upload it on github

chunk_size <- 100000

num_chunks <- ceiling(nrow(tripdata) / chunk_size)

for (i in 1:num_chunks) {
  # Calculate the starting and ending row for each chunk
  start_row <- ((i - 1) * chunk_size) + 1
  end_row <- min(i * chunk_size, nrow(tripdata))
  
  # Subset the data for this chunk
  chunk <- tripdata[start_row:end_row, ]
  
  # Write each chunk to a separate CSV file
  write.csv(chunk, paste0("tripdata", i, ".csv"), row.names = FALSE)
}