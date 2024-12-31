from django import template
import re

register = template.Library()


def embed_video(text):
    """
        Detect and embed video links for YouTube, TikTok, Instagram, Facebook, and other platforms.
    """

    # Regular expressions for various platforms
    youtube_regex = r'(https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+|https?://(?:www\.)?youtu\.be/[\w-]+)'
    tiktok_regex = r'(https?://(?:www\.)?tiktok\.com/@[\w.-]+/video/[\d]+)'
    instagram_regex = r'(https?://(?:www\.)?instagram\.com/p/[\w-]+)'
    facebook_regex = r'(https?://(?:www\.)?facebook\.com/.+/videos/[\d]+)'
    video_file_regex = r'(https?://[^\s]+\.mp4|https?://[^\s]+\.webm|https?://[^\s]+\.ogg)'

    # Embedding logic for each platform
    def youtube_embed(match):
        video_id = match.group(0).split('v=')[-1].split('&')[0]
        return f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'

    def tiktok_embed(match):
        video_id = match.group(0).split('/video/')[-1]
        return f'<iframe src="https://www.tiktok.com/embed/{video_id}" width="325" height="575" frameborder="0" allowfullscreen></iframe>'

    def instagram_embed(match):
        return f'<iframe src="{match.group(0)}embed/" width="400" height="480" frameborder="0" allowfullscreen></iframe>'

    def facebook_embed(match):
        return f'<iframe src="https://www.facebook.com/plugins/video.php?href={match.group(0)}" width="560" height="315" frameborder="0" allowfullscreen></iframe>'

    def video_file_embed(match):
        return f'<video controls width="560"><source src="{match.group(0)}" type="video/mp4">Your browser does not support the video tag.</video>'

    # Apply each regex and replace links with embed code
    text = re.sub(youtube_regex, youtube_embed, text)
    text = re.sub(tiktok_regex, tiktok_embed, text)
    text = re.sub(instagram_regex, instagram_embed, text)
    text = re.sub(facebook_regex, facebook_embed, text)
    text = re.sub(video_file_regex, video_file_embed, text)

    return text


register.filter('embed_video', embed_video)
