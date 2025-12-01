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
    
  0)

(defun part2 (lines)
  0)

(defun main ()
  (let ((lines (read-input "input.txt")))
    (format t "Part 1: ~a~%" (part1 lines))
    (format t "Part 2: ~a~%" (part2 lines))))
