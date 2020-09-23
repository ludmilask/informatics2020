while True
do
	total=$(($(ls -lA ./custom_tmp | wc -l) - 1))
	folders=$(ls -lA ./custom_tmp | grep -c ^d)
	printf "Contents of custom_tmp: %d files, %d folders\n" $(($total-$folders)) $folders
	sleep 1s
done
