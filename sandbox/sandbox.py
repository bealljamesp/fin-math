def area_of_circle(r):
    import numpy as np
    from scipy import integrate

    # define the limits of integration
    theta_min = 0
    theta_max = 2 * np.pi
    r_min = 0
    r_max = r

    # define the integrand in polar coordinates
    def integrand(r, theta):
        return r

    # perform the double integration
    area, error = integrate.dblquad(
        integrand, theta_min, theta_max, lambda theta: r_min, lambda theta: r_max
    )

    return area
