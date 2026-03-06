# Image Setup Guide for IBR Foundation Site

## Where to Add Your Images

All images should be placed in: `core/static/images/`

## Required Images

### 1. **Logo Image** (REQUIRED)
- **File name:** `logo.png`
- **Location:** `core/static/images/logo.png`
- **Recommended size:** 200px × 50px (width × height)
- **Format:** PNG with transparent background (recommended)
- **Purpose:** Displays in the top-left navbar

### 2. **Hero Background Image** (OPTIONAL)
- **File name:** `hero-bg.jpg`
- **Location:** `core/static/images/hero-bg.jpg`
- **Recommended size:** 1920px × 1080px (or larger)
- **Format:** JPG or PNG
- **Purpose:** Background image for the hero section

## How to Add Images

1. Copy your image files to: `core/static/images/`
2. Restart the Django server (if needed)
3. The images will automatically load on the site

## Image Specifications

### Logo
- Should be a PNG with transparent background
- Recommended: 200-300px wide, auto height
- Your organization's logo or brand icon
- Works best as a clear, recognizable image

### Hero Background
- High-resolution photo or image
- Should be engaging and relevant to your mission
- A darker image works better with the overlay
- Can be a community photo, team photo, or abstract design

## Multiple Images per Section

To add multiple images to different sections:

1. **Projects Section** - You can add images to project cards by modifying `core/views.py` and adding image paths
2. **Other Sections** - Contact us for custom image placement

## If Images Don't Load

Make sure:
- File names match exactly (case-sensitive on some servers)
- Images are in `core/static/images/` folder
- File format matches the extension
- Run `python manage.py collectstatic` (for production)

## Example File Structure

```
IBR_Group/
├── core/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── images/
│   │       ├── logo.png          ← Your logo here
│   │       ├── hero-bg.jpg       ← Hero background here
│   │       └── (other images)
│   ├── templates/
│   └── ...
```

## Need Help?

Contact us or check the Django static files documentation for more details.
