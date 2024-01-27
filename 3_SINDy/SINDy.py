from numpy import abs, real, imag, zeros
from numpy.linalg import lstsq as least_squares

def sindy(df_, features, target, cut_tol=0.005):

    df = df_[features+[target]].copy()
    column_names = features.copy()
    columns_used = column_names.copy()

    converged=False
    while not converged:

        # Compute the coefficients with least squares
        columns_used_before = columns_used.copy()
        A = df[columns_used].values
        B = df[target].values
        coef = least_squares(A,B,rcond=None)[0]

        # Remove columns with low coefficients
        for i in range(len(coef)):
            if abs(coef[i]) < cut_tol:
                coef[i] = 0
                df[columns_used_before[i]] = zeros(len(df))
                if columns_used_before[i] in columns_used:
                    columns_used.remove(columns_used_before[i])
        
        # Converge when the used columns stay the same
        if tuple(columns_used_before) == tuple(columns_used):
            converged = True

    # Remove imaginary or real not used parts
    for i, c in enumerate(coef):
        if abs(real(c)) < cut_tol:
            coef[i] = 1j*imag(c)
        if abs(imag(c)) < cut_tol:
            coef[i] = real(c)

    return columns_used, coef

