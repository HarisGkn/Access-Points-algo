import math

def calculate_access_points(num_services, sampling_rates, bits_per_sample, capacity):
    
    #num_services: number of services.
    #sampling_rates: sampling rates for each service.
    #bits_per_sample: number of bits per sample
    #capacity: bit rate capacity 
    #min_access_points: minimum number of access points required
    
    # input validation
    if not (len(sampling_rates) == len(bits_per_sample) == num_services):
        raise ValueError("The number of services does not match the size of the sampling_rates and bits_per_sample lists.")

    if capacity <= 0:
        raise ValueError("The capacity of the access point must be positive.")

    total_bit_rate = sum(sampling_rates[i] * bits_per_sample[i] for i in range(num_services))

    # Use math.ceil to round up and ensure sufficient capacity
    min_access_points = math.ceil(total_bit_rate / capacity)

    return min_access_points

try:
    #prompt the user for all the required inputs
    num_services = int(input("Enter the number of services: "))
    sampling_rates = [int(input(f"Enter the sampling rate for service {i+1}: ")) for i in range(num_services)]
    bits_per_sample = [int(input(f"Enter the number of bits per sample for service {i+1}: ")) for i in range(num_services)]
    capacity = int(input("Enter the bit rate capacity of an access point: "))
    
    # Calculate and print the minimum number of access points required 
    min_access_points = calculate_access_points(num_services, sampling_rates, bits_per_sample, capacity)
    print(f"Minimum number of access points required: {min_access_points}")
except ValueError as e:
    # Handle any input errors
    print(f"Error: {e}")

input("Press Enter to exit")

