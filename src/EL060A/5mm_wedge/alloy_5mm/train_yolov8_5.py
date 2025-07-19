from ultralytics import YOLO
import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_loss_curves(run_dir):
    results_file = os.path.join(run_dir, 'results.csv')
    
    # Read the results.csv file
    results = pd.read_csv(results_file)
    
    # Plot the loss curves
    plt.figure(figsize=(10, 5))

    # Plot training and validation box loss
    plt.subplot(1, 2, 1)
    plt.plot(results['epoch'], results['train/box_loss'], label='Train Box Loss')
    plt.plot(results['epoch'], results['val/box_loss'], label='Val Box Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Box Loss')
    plt.legend()
    plt.title('Box Loss')

    # Plot training and validation object loss
    plt.subplot(1, 2, 2)
    plt.plot(results['epoch'], results['train/obj_loss'], label='Train Obj Loss')
    plt.plot(results['epoch'], results['val/obj_loss'], label='Val Obj Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Obj Loss')
    plt.legend()
    plt.title('Obj Loss')

    plt.tight_layout()
    plt.show()

def main():
    # Define the path to the data.yaml file
    data_yaml_path = '/Users/chootydoony/Documents/Miun/EL035A_Project/src/alloy_5mm/data5.yaml'

    # Check if yolov8n.pt exists, otherwise download it
    model_path = "yolov8n.pt"
    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}. Downloading...")
        model = YOLO(model_path)  # This will trigger the download
    else:
        model = YOLO(model_path)  # Load the existing model

    # Set training parameters
    epochs = 150
    imgsz = 800  # Start with 800
    batch = 4  # Batch size of 4 to fit memory constraints
    workers = 1  # Number of data loading workers (adjust based on your system)


    # Define the path to save checkpoints
    checkpoint_dir = '/Users/chootydoony/Documents/Miun/EL035A_Project/src/alloy_5mm/runs_5/train_experiment'
    os.makedirs(checkpoint_dir, exist_ok=True)

    # Train the model
    model.train(
        data=data_yaml_path, 
        epochs=epochs, 
        imgsz=imgsz, 
        batch=batch, 
        project=checkpoint_dir, 
        name='train_experiment',
        save_period=10  # Save checkpoints every 10 epochs
    )
    
    # Validate the model
    model.val()

    # Save the trained model
    model.save("yolov8n_trained5.pt")

    # Plot the loss curves
    plot_loss_curves(checkpoint_dir)  # Update the path if necessary

if __name__ == "__main__":
    main()
