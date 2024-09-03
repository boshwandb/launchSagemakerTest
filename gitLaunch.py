import wandb

def log_artifact():
    # Initialize a W&B run
    run = wandb.init(project="artifact_example", entity="your_entity_name")

    # Create an artifact
    artifact = wandb.Artifact(name="example-artifact", type="dataset")
    
    # Add the file to the artifact
    artifact.add_file("/mnt/datasets/100Chairs_128renders/example.txt")

    # Log the artifact to W&B
    run.log_artifact(artifact)
    
    # Finish the run
    run.finish()

if __name__ == "__main__":
    log_artifact()