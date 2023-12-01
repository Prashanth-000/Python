import matplotlib.pyplot as plt
import random
import time

def bubble_sort(data):
    n=len(data)
    for i in range(n):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                plt.bar(range(len(data)),data,color='yellow')
                plt.title('Bubble sort animation')
                plt.pause(0.2)
                plt.clf()
                plt.bar(range(len(data)),data,color='green')

def generate_data(size):
    return [random.randint(1,100) for i in range(size)]

def main():
    size = 30
    data=generate_data(size)

    plt.figure(figsize=(8,6))
    plt.bar(range(len(data)),data,color='blue')
    plt.title('Before sorting')
    plt.show()

    bubble_sort(data)
    
    plt.figure(figsize=(8,6))
    plt.bar(range(len(data)),data,color='pink')
    plt.title('After sorting')
    plt.show()

if __name__ == "__main__":
        
    main()

