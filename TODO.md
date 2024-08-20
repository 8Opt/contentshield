text-model (binary/multi-class)
+ DistilBERT.
+ ALBERT.
+ Qwen-0.5. (Qwen/Qwen1.5-0.5B)

image-model (detection only): 
+ YOLO.


## Folder Stucture

```text
/assets                     # Save static files: images, notebooks, etc.
/contentshield
    model_config            # Configuration of all supported-models.
    /elements               # 
    /detector               # Define models for classifying and detecting harmful content.
        text
        image
    /tools                  # Methods for augmenting input (text, image) and others(translation, etc.)
    /stategies              # Define logics to handle harmful content: notify, eliminate, augment ouput, etc. 
/test
```

# Roadmap

# Resources

## Audio

+ [PySceneDetect](https://www.scenedetect.com/docs/latest/api/detectors.html)