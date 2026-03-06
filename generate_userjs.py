import random
import string
import sys

def rand(arr): return random.choice(arr)
def rand_int(a,b): return random.randint(a,b)
def rand_bool(): return "true" if random.random() > 0.5 else "false"
def rand_string(n=16): return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))

# Browser UA templates for desktop
desktop_browsers = [
    "Mozilla/5.0 ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "Mozilla/5.0 ({platform}; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/95.0.0.0",
    "Mozilla/5.0 ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Brave/123.0.0.0"
]

# Desktop OS profiles
ua_profiles = [
    {
        "name": "Windows Desktop",
        "platform": "Win32",
        "oscpu": "Windows NT 10.0; Win64; x64",
        "webgl_vendor": "Google Inc.",
        "webgl_renderer": "ANGLE (NVIDIA GeForce GTX 1060 Direct3D11 vs_5_0 ps_5_0)",
        "font_whitelist": "Arial, Times New Roman, Courier New",
        "permissions": {"camera":"2","microphone":"2","geo":"2","notif":"2"},
        "touch":"0","pointer":"true","hover":"hover",
        "win_size": (rand_int(1280,1920), rand_int(720,1080)),
        "media_codecs": ["H.264","VP9","Opus","AAC"],
        "mime_audio": ["audio/mp3","audio/wav","audio/ogg"],
        "mime_video": ["video/mp4","video/webm","video/ogg"],
        "plugins": "Shockwave Flash, Widevine CDM, PDF Viewer",
        "accept_encoding": "gzip, deflate, br",
        "color_profile": "sRGB.icc"
    },
    {
        "name": "Linux Desktop",
        "platform": "Linux x86_64",
        "oscpu": "Linux x86_64",
        "webgl_vendor": "Mesa Project",
        "webgl_renderer": "Mesa DRI Intel UHD Graphics",
        "font_whitelist": "Roboto, DejaVu Sans, Liberation Sans",
        "permissions": {"camera":"2","microphone":"2","geo":"2","notif":"2"},
        "touch":"0","pointer":"true","hover":"hover",
        "win_size": (rand_int(1280,1920), rand_int(720,1080)),
        "media_codecs": ["VP9","Opus","Vorbis"],
        "mime_audio": ["audio/ogg","audio/flac"],
        "mime_video": ["video/webm","video/ogg"],
        "plugins": "Widevine CDM, PDF Viewer",
        "accept_encoding": "gzip, deflate",
        "color_profile": "DisplayP3.icc"
    },
    {
        "name": "macOS Desktop",
        "platform": "MacIntel",
        "oscpu": "Intel Mac OS X 12.3",
        "webgl_vendor": "Apple",
        "webgl_renderer": "Apple GPU",
        "font_whitelist": "Helvetica, Geneva, Tahoma",
        "permissions": {"camera":"2","microphone":"2","geo":"2","notif":"2"},
        "touch":"0","pointer":"true","hover":"hover",
        "win_size": (rand_int(1280,1920), rand_int(720,1080)),
        "media_codecs": ["H.264","AAC","Opus"],
        "mime_audio": ["audio/aac","audio/mp3"],
        "mime_video": ["video/mp4","video/av1"],
        "plugins": "Widevine CDM, PDF Viewer",
        "accept_encoding": "br, gzip",
        "color_profile": "DisplayP3.icc"
    }
]

# Other pools
languages = ["en-US","fr-FR","de-DE","es-ES","ja-JP","ko-KR","zh-CN","pt-BR"]
timezones = ["UTC","Europe/Paris","America/New_York","Asia/Tokyo","Australia/Sydney"]
dpis = [
  "1.190","1.174","1.150","1.136","1.118","1.153","1.177","1.167","1.119","1.121",
  "1.115","1.187","1.186","1.176","1.183","1.170","1.182","1.141","1.162","1.145",
  "1.143","1.156","1.155","1.172","1.122","1.154","1.137","1.191","1.194","1.113",
  "1.161","1.130","1.114","1.151","1.142","1.175","1.140","1.168","1.146","1.158",
  "1.169","1.159","1.135","1.148","1.184","1.125","1.157","1.199","1.152","1.112",
  "1.144","1.173","1.178","1.189","1.131","1.195","1.160","1.132","1.133","1.193",
  "1.171","1.111","1.166","1.197","1.180","1.185","1.123","1.196","1.188","1.179",
  "1.149","1.163","1.126","1.138","1.192","1.116","1.127","1.117","1.165","1.128",
  "1.134","1.200","1.124","1.139","1.129","1.198","1.147","1.181","1.120","1.164"
]
dprs = [
  "1.190","1.174","1.150","1.136","1.118","1.153","1.177","1.167","1.119","1.121",
  "1.115","1.187","1.186","1.176","1.183","1.170","1.182","1.141","1.162","1.145",
  "1.143","1.156","1.155","1.172","1.122","1.154","1.137","1.191","1.194","1.113",
  "1.161","1.130","1.114","1.151","1.142","1.175","1.140","1.168","1.146","1.158",
  "1.169","1.159","1.135","1.148","1.184","1.125","1.157","1.199","1.152","1.112",
  "1.144","1.173","1.178","1.189","1.131","1.195","1.160","1.132","1.133","1.193",
  "1.171","1.111","1.166","1.197","1.180","1.185","1.123","1.196","1.188","1.179",
  "1.149","1.163","1.126","1.138","1.192","1.116","1.127","1.117","1.165","1.128",
  "1.134","1.200","1.124","1.139","1.129","1.198","1.147","1.181","1.120","1.164"
]
color_depths = [8,16,24,30]
orientation_angles = ["0","90","180","270"]
orientation_types = ["portrait-primary","portrait-secondary","landscape-primary","landscape-secondary"]
audio_rates = [44100,48000,32000,22050]
webrtc_flags = ["true","false"]
battery_levels = ["0.25","0.50","0.75","1.0"]
battery_charging = ["true","false"]
pointer_enabled = ["true","false"]
hover_capabilities = ["none","hover","on-demand"]

canvas_seed = rand_int(100000,999999)
os_builds = ["20240201000000","20231015000000","20221201000000","20230101000000"]

# Load template
with open("template-userjs.txt","r",encoding="utf-8") as f:
    template = f.read()

# === Pick a profile and assign UA ===
profile = rand(ua_profiles)
ua_template = rand(desktop_browsers)
profile["ua"] = ua_template.format(platform=profile["platform"])

# Randomize some values
dpr = rand(dprs)
color_depth = rand(color_depths)
orientation_angle = rand(orientation_angles)
orientation_type = rand(orientation_types)


# === Replace placeholders ===
output = (
    template
    .replace("__UA__", profile["ua"])
    .replace("__PLATFORM__", profile["platform"])
    .replace("__OSCPU__", profile["oscpu"])
    .replace("__WEBGL_VENDOR__", profile["webgl_vendor"])
    .replace("__WEBGL_RENDERER__", profile["webgl_renderer"])
    .replace("__FONT_WHITELIST__", profile["font_whitelist"])
    .replace("__PERM_CAMERA__", profile["permissions"]["camera"])
    .replace("__PERM_MIC__", profile["permissions"]["microphone"])
    .replace("__PERM_GEO__", profile["permissions"]["geo"])
    .replace("__PERM_NOTIF__", profile["permissions"]["notif"])
    .replace("__TOUCH__", profile["touch"])
    .replace("__POINTER_ENABLED__", profile["pointer"])
    .replace("__HOVER_CAPABILITY__", profile["hover"])
    .replace("__WIN_W__", str(profile["win_size"][0]))
    .replace("__WIN_H__", str(profile["win_size"][1]))
    .replace("__LANG__", rand(languages))
    .replace("__LOCALE__", rand(languages))
    .replace("__TIMEZONE__", rand(timezones))
    .replace("__DPI__", rand(dpis))
    .replace("__DPR__", dpr)
    .replace("__COLOR_DEPTH__", str(color_depth))
    .replace("__ORIENTATION_ANGLE__", orientation_angle)
    .replace("__ORIENTATION_TYPE__", orientation_type)
    .replace("__CORES__", str(rand_int(2,16)))
    .replace("__WEBGL__", rand_bool())
    .replace("__WEBGLMIN__", rand_bool())
    .replace("__CANVAS_SEED__", str(canvas_seed))
    .replace("__DOCFONTS__", str(rand_int(0,1)))
    .replace("__DLFONTS__", rand_bool())
    .replace("__WEBAUDIO__", rand_bool())
    .replace("__AUDIO_RATE__", str(rand(audio_rates)))
    .replace("__PERM_CAMERA__", profile["permissions"]["camera"])
    .replace("__PERM_MIC__", profile["permissions"]["microphone"])
    .replace("__PERM_GEO__", profile["permissions"]["geo"])
    .replace("__PERM_NOTIF__", profile["permissions"]["notif"])
    .replace("__AUDIO_DEVICE_ID__", rand_string(24))
    .replace("__VIDEO_DEVICE_ID__", rand_string(24))
    .replace("__OS_BUILD__", rand(os_builds))
    .replace("__ACCEPT_ENCODING__", profile["accept_encoding"])
    .replace("__COLOR_PROFILE__", profile["color_profile"])
    .replace("__MIME_AUDIO__", rand(profile["mime_audio"]))
    .replace("__MIME_VIDEO__", rand(profile["mime_video"]))
    .replace("__PLUGIN_LIST__", profile["plugins"])
    .replace("__WEBRTC_ENABLED__", rand(webrtc_flags))
    .replace("__WEBRTC_NO_HOST__", rand(webrtc_flags))
    .replace("__WEBRTC_DEFAULT_ONLY__", rand(webrtc_flags))
    .replace("__NAV_APPNAME__", rand(["Netscape","Mozilla","Firefox"]))
    .replace("__NAV_APPVERSION__", rand(["5.0","4.0","3.1"]))
    .replace("__NAV_BUILDID__", rand(["20240201","20231015","20221201"]))
    .replace("__BATTERY_LEVEL__", rand(battery_levels))
    .replace("__BATTERY_CHARGING__", rand(battery_charging))
    .replace("__POINTER_ENABLED__", rand(pointer_enabled))
    .replace("__HOVER_CAPABILITY__", rand(hover_capabilities))
)

# === Save output ===
with open("user.js","w",encoding="utf-8") as f:
    f.write(output)

print(f"Generated user.js with consistent profile: {profile['name']}")
