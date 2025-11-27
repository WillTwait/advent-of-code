(defun read-input (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
          while line
          collect line)))

(defun part1 (lines)
  0)

(defun part2 (lines)
  0)

(defun main ()
  (let ((lines (read-input "input.txt")))
    (format t "Part 1: ~a~%" (part1 lines))
    (format t "Part 2: ~a~%" (part2 lines))))

(main)
