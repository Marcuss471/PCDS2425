import numpy as np
import matplotlib.pyplot as plt

# PART A
# A:1
def A1():
    type = np.asarray([1, 2, 3])
    counts = np.asarray([2, 3, 195])
    urn = np.repeat(type, counts)

    N = 100 # Draw 100 times
    draw_replacement = np.random.choice(urn, size=N, p=None, replace=True)
    print(draw_replacement) # [3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
                            # 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
                            # 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 2]


# A:2
def A2():
    cassette_sample = np.asarray([54, 66, 70, 72, 97])
    sample_count = np.asarray([5] * 5)
    cassette = np.repeat(cassette_sample, sample_count)

    N = 1000
    draw_replacement = np.random.choice(cassette, size=(N, 3), p=None, replace=True)
    row_sum = draw_replacement.sum(axis=1)  # Sums each row for the total time
    above_200 = np.sum(row_sum > 200)       # Counts how many of the rows are above 200 minutes

    print(f"Number of cassettes over 200: {above_200}")     # Number of cassettes over 200: 699
    print(f"Number of cassettes: {N}")                      # Number of cassettes: 1000
    print(f"Fraction: {above_200/N}")                       # Fraction: 0.699


# A:3
def A3():
    def iterations(urn, replacement):
        N = 10000
        non_faulty_counter = 0
        
        for _ in range(N):
            draw_balls = np.random.choice(urn, size=3, p=None, replace=replacement)
            if np.all(draw_balls == "white"):
                non_faulty_counter += 1
                
        return non_faulty_counter/N
    
    # (a)
    ball_color_a = np.asarray(["red", "white"])
    ball_count_a = np.asarray([4, 8])
    ballpit_a = np.repeat(ball_color_a, ball_count_a)

    # (b)
    ball_color_b = np.asarray(["red", "white"])
    ball_count_b = np.asarray([400, 800])
    ballpit_b = np.repeat(ball_color_b, ball_count_b)
    
    # (c)
    ball_color_c = np.asarray(["red", "white"])
    ball_count_c = np.asarray([1, 2])
    ballpit_c = np.repeat(ball_color_c, ball_count_c)

    # printing
    print(f"fraction of 4/8: {iterations(ballpit_a, False)}")
    print(f"fraction of 400/800: {iterations(ballpit_b, False)}")
    print(f"fraction of 1/2: {iterations(ballpit_c, True)}")
        # fraction of 4/8: 0.254
        # fraction of 400/800: 0.2974
        # fraction of 1/2: 0.2936
    
    # (d)
    # (a) is not similar the others because it has a much smaller urn to pick from.
    # (c) has a smaller urn than (a) but it has replacement so when it's drawing from the urn it dosen't effect the next draw.
    # (b) has a big urn so when a ball is drawn it dosen't affect the next drawing as much.
    # When (a) is drawn, the odds for the next drawing is significant.


# A:4
def A4():
    ball_color = np.asarray(['red', 'white'])
    ball_count = np.asarray([93, 7])
    balls = np.repeat(ball_color, ball_count)
    
    N = 1000
    well_draw = np.random.choice(balls, size=(N, 96), p=None, replace=True)
    freq_red = np.sum(well_draw == 'red', axis=1)
    
    mean = np.mean(freq_red)
    min = np.min(freq_red)
    max = np.max(freq_red)
    
    print(f"Average number of redballs: {mean}")
    # print(min)
    # print(max)
    
    plt.hist(freq_red, bins=(range(min, max)), edgecolor="black")
    plt.title("Histogram - Number of Red Balls")
    plt.ylabel("Frequency")
    plt.xlabel("number of red balls")
    plt.show()


# B:1
def B1():
    def N(my, sigma, x):
        return ((1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(1/(2*sigma**2))*(x-my)**2))
    
    # def Beta(alpha, beta, x):
    #     return ((x**(alpha-1)*(1-x)**(beta-1))/())
    
    # def Weibull(k, lambda_):
    #     return
    
    
    
    
    # normal_dis = np.random.normal(loc=my, scale=sigma, size=size_)
    # normal_x = np.linspace(min(normal_dis), max(normal_dis), size_)
    # normal_pdf = (1 / (np.sqrt(2*np.pi))) * np.exp(-0.5 * normal_x**2)
    # # plt.plot(normal_x, normal_pdf, label="Normal distrubution PDF")
    
    # beta_dis = np.random.beta(alpha, beta, size=size_)
    # beta_x = np.linspace(min(beta_dis), max(beta_dis), size_)
    # beta_pdf = (beta_x**(alpha-1)*(1-beta_x)**(beta-1)) / beta_dis
    # plt.plot(beta_x, beta_pdf, label="Beta distrubution PDF")

    
    # plt.legend()
    # plt.show()
    
    my = 0
    sigma = 2
    alpha = 2
    beta = 5
    lambda_ = 1
    k = 1.5
    size_ = 1000

    # Create figure with three subplots
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    x = np.linspace(-5, 5, size_)
    normal_pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - my) ** 2) / (2 * sigma ** 2))
    axes[0].plot(x, normal_pdf, color="green", label="Normal PDF")
    axes[0].set_title('Normal Distribution')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('PDF')
    axes[0].legend()
    axes[0].grid()

    # Beta Distribution PDFs (manually defined)
    # x = np.linspace(0, 1, size_)
    beta_params = [(0.5, 0.5), (5, 1), (1, 3), (2, 2), (2, 5)]

    def beta_pdf(x, alpha, beta):
        coeff = (x ** (alpha - 1)) * ((1 - x) ** (beta - 1))
        return coeff / np.trapz(coeff, x)  # Normalize so it integrates to 1

    # for alpha, beta_ in beta_params:
    #     axes[1].plot(x, beta_pdf(x, alpha, beta_), label=rf'$\alpha={alpha}, \beta={beta_}$')
    axes[1].plot(x, beta_pdf(x, alpha, beta), color="blue", label=f'alpha={alpha}, beta={beta}')
    axes[1].set_title('Beta Distribution')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('PDF')
    axes[1].legend()
    axes[1].grid()

    # Weibull Distribution PDFs (manually defined)
    # x = np.linspace(0, 2.5, size_)
    weibull_params = [0.5, 1, 1.5, 5]

    def weibull_pdf(x, k, lam):
        return (k / lam) * (x / lam) ** (k - 1) * np.exp(-(x / lam) ** k)

    # for k in weibull_params:
    #     axes[2].plot(x, weibull_pdf(x, k), label=rf'$\lambda=1, k={k}$')
    axes[2].plot(x, weibull_pdf(x, k, lambda_), color="red", label=f'lambda={lambda_}, k={k}')
    axes[2].set_title('Weibull Distribution')
    axes[2].set_xlabel('x')
    axes[2].set_ylabel('PDF')
    axes[2].legend()
    axes[2].grid()

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()

    
    
    
    pass



if __name__ == "__main__":
    A1()
    
    A2()
    
    A3()
    
    A4()
    
    B1()
    
    pass