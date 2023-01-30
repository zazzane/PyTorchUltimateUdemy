#%%
from ultralytics import YOLO
# %% Load a model
model = YOLO("masks.pt")  # load our custom trained model

# %%
result = model("test/images/maksssksksss843.png")
# %%
result
# %% command line run
# Standard Yolo
!yolo detect predict model=yolov8n.pt source="test/kiki.jpg" conf=0.3 
# %% Masks 
!yolo detect predict model=train_custom/masks.pt source="train_custom/test/images/IMG_0742.MOV" conf=0.3 

# %%
