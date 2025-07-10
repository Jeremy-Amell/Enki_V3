from encoding_chi import main as run_chi_encoding
from encoding_theta import main as run_theta_encoding
from encoding_lambda import main as run_lambda_encoding
from encoding_epsilon import main as run_epsilon_encoding

def main():
    print("\nRunning Chi Encoding...")
    run_chi_encoding()
    print("Chi Encoding Complete.\n")

    print("Running Theta Encoding...")
    run_theta_encoding()
    print("Theta Encoding Complete.\n")

    print("Running Lambda Encoding...")
    run_lambda_encoding()
    print("Lambda Encoding Complete.\n")

    print("Running Epsilon Encoding...")
    run_epsilon_encoding()
    print("Epsilon Encoding Complete.\n")


if __name__ == "__main__":
    main()