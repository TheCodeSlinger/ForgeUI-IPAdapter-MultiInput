import gradio as gr
from modules import scripts, processing
from modules.processing import StableDiffusionProcessingImg2Img
from PIL import Image
import numpy as np
import re

class ForgeIpAdapterMulti(scripts.Script):
    def __init__(self):
        super().__init__()

    def title(self):
        return "Forge IpAdapter Multi-Input"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Accordion("Forge IpAdapter Multi-Input", open=False):
            enabled = gr.Checkbox(label="Enable Multi-Image Input")
            multi_images = gr.File(
                label="Upload Multiple Images",
                type="filepath",
                file_count="multiple",
                file_types=["image"]
            )
        return [enabled, multi_images]

    def process(self, p: StableDiffusionProcessingImg2Img, enabled, multi_images):
        # Only proceed if the extension is enabled
        if not enabled:
            return

        # Ensure multiple images have been provided
        if not multi_images or len(multi_images) == 0:
            print("No images provided for multi-image input.")
            return

        # Convert file paths to numpy arrays
        image_arrays = []
        for image_path in multi_images:
            try:
                img = Image.open(image_path).convert('RGBA')
                image_arrays.append(np.array(img))
            except Exception as e:
                print(f"Error loading image {image_path}: {e}")
                continue

        if len(image_arrays) == 0:
            print("No valid images were loaded.")
            return

        # Replace extra_result_images with our images
        p.extra_result_images = image_arrays

        # Iterate over the items in p.script_args_value
        for idx, item in enumerate(p.script_args_value):
            if hasattr(item, 'model') and hasattr(item, 'input_mode'):
                if 'ip-adapter' in item.model.lower():
                    # Set input_mode to 'merge'
                    item.input_mode = 'merge'

                    # Assign the list of images
                    item.images = image_arrays  # Use the numpy array images

                    # Clear the single image
                    item.image = None

                    # Update extra_generation_params
                    controlnet_key = f'ControlNet {idx}'
                    if controlnet_key in p.extra_generation_params:
                        # Parse the existing parameter string and update Input Mode
                        param_str = p.extra_generation_params[controlnet_key]
                        # Update Input Mode
                        if 'Input Mode:' in param_str:
                            new_param_str = re.sub(r'Input Mode: \w+', 'Input Mode: merge', param_str)
                        else:
                            # Append Input Mode if it's not present
                            new_param_str = param_str + ', Input Mode: merge'
                        p.extra_generation_params[controlnet_key] = new_param_str
                    else:
                        # If the key doesn't exist, add it with updated parameters
                        p.extra_generation_params[controlnet_key] = (
                            f"Module: {item.module}, Model: {item.model}, Weight: {item.weight}, "
                            f"Resize Mode: {item.resize_mode}, Processor Res: {item.processor_res}, "
                            f"Threshold A: {item.threshold_a}, Threshold B: {item.threshold_b}, Guidance "
                            f"Start: {item.guidance_start}, Guidance End: {item.guidance_end}, "
                            f"Pixel Perfect: {item.pixel_perfect}, Control Mode: {item.control_mode}, Hr "
                            f"Option: {item.hr_option}, Input Mode: merge"
                        )

                    # Log the update for debugging
                    print(f"Updated ControlNetUnit with model '{item.model}' to use merge mode with {len(image_arrays)} images.")
            else:
                continue

        # For debugging: print the updated extra_generation_params and extra_result_images
        print("Updated extra_generation_params:")
        for key, value in p.extra_generation_params.items():
            print(f"{key}: {value}")
        print(f"Total images in extra_result_images: {len(p.extra_result_images)}")