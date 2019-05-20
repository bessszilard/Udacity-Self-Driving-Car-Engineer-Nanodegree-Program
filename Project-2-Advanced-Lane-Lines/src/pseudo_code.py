input: poly_x, poly_y
if fifo not empty:
	error = lsq_e( recently_fitted_x, poly_x )
	if error < 20%:
		# valid result
		current_fit = np.polyfit(poly_y, poly_x, 2)
		if len(current_fit) == 0:
			return recently_fitted_x, poly_y
		elif len(fifo) > fifo_max_len:
			fifo.pop(0)
		fifo.append([current_fit])
		
		avg_fit = avg(fifo)
		recently_fitted_x = generate_x(avg_fit)
		return recently_fitted_x, poly_y
	else:
		return recently_fitted_x, poly_y
#fifo is empty
else:
	current_fit = np.polyfit(poly_y, poly_x, 2)
	fifo.append([current_fit])
	recently_fitted_x = generate_x(current_fit)
	return current_fit, poly_y
	
	
TODO
	leftx, rightx are not empty