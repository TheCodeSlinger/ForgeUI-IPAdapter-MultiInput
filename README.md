# ForgeUI-IPAdapter-MultiInput

### Overview

**ForgeUI-IPAdapter-MultiInput** is an extension for the [ForgeUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) platform, designed to add support for multiple image inputs when using the **IP-Adapter** models within the ControlNet framework. This extension allows users to merge multiple images into the input pipeline, enhancing the control and flexibility of image generation workflows in ForgeUI.

By default, ForgeUI only allows a single image input when working with ControlNet, which limits the ability to apply complex guidance from multiple sources. This extension overcomes that limitation by adding an option to upload multiple images and seamlessly integrates them into the pipeline for IP-Adapter models.

### Features

- **Multiple Image Input**: Users can upload multiple images instead of a single one when using ControlNet models such as IP-Adapter.
- **Automatic Merge Mode**: The extension automatically sets the input mode to 'merge' for IP-Adapter models when multiple images are provided.
- **UI Enhancements**: Simple checkbox to enable/disable the multi-image input functionality, with easy-to-use file upload support.
- **Extends ForgeUI's Capabilities**: Allows for more complex and nuanced image generation workflows when using IP-Adapter models, ideal for cases where multiple sources of guidance are required.

### Why I Made This

I created this extension because I noticed that the current implementation of **ForgeUI** lacked the ability to take multiple image inputs for the **IP-Adapter** models, which significantly limits its potential for certain use cases. The ability to combine multiple images as input can be very useful in scenarios where more complex image generation is needed, particularly when working with model-guided transformations like those available in **ControlNet**.

Without this extension, users were forced to either:
- Use a batch mode that processes images separately (not truly merging them as one input).
- Manually process and merge images before using them in ForgeUI, which can be tedious and inefficient.

This extension aims to streamline that process by:
- Providing a **multi-image input mode** directly within the ForgeUI interface.
- Automatically handling the ControlNet parameters to support multiple images, making it a plug-and-play solution for ForgeUI users.

### Installation

To install this extension:

1. Clone the repository into the `extensions` directory of your ForgeUI installation:
   ```bash
   git clone https://github.com/TheCodeSlinger/ForgeUI-IPAdapter-MultiInput.git
