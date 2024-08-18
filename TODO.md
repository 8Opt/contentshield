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
    /schema
    /detector
        /text               # Focus only small-text like Facebook's, Reddit's post. 
        /image
        /video
        /audio
    /processor
        /preprocessing      # Including cleaning text, resize images, scene detects, etc.
        /postprocessing     # Including define a set of rule for latst outputs
    /stategies              # Simple pipelines for detecting harmful content
/test
```


# Resources

## Audio

+ [PySceneDetect](https://www.scenedetect.com/docs/latest/api/detectors.html)