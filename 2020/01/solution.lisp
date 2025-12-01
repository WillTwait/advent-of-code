(defun read-input (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
          while line
          collect (parse-integer line))))

(defun make-num-set (nums)
  (let ((ht (make-hash-table)))
    (loop for n in nums do
      (setf (gethash n ht) t))
    ht
    ))

(defun part1 (lines)
  (let ((num-set (make-num-set lines)))
    (loop for n in lines
	  for pair = (- 2020 n)
	  when (gethash pair num-set)
	    return (* n pair)
	    ))
)

(defun part2 (lines)
  (let ((num-set (make-num-set lines)))
    (loop for n in lines
	  for sum = (- 2020 n) do
	    (loop for i in lines
		  for final-sum = (- sum i)
		  when (gethash final-sum num-set)
		    do (return-from part2 (* final-sum i n))
	  )))
  )

(defun main ()
  (let ((lines (read-input "input.txt")))
    (format t "Part 1: ~a~%" (part1 lines))
    (format t "Part 2: ~a~%" (part2 lines))))
