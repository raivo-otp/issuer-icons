
<p align="center">
    <img src="https://raw.githubusercontent.com/raivo-otp/ios-application/master/Assets/app-icon.png" width="200"/>
</p>
<h1 align="center">Raivo OTP issuer icons</h1>
<p align="center">
    <a href="https://github.com/raivo-otp/ios-application/blob/master/LICENSE.md"><img src="https://raw.finnwea.com/shield/?firstText=License&secondText=CC%20BY-NC%204.0" /></a>
    <a href="https://travis-ci.org/raivo-otp/issuer-icons"><img src="https://raw.finnwea.com/vector-shields-v1/?typeKey=TravisBuildStatus&typeValue1=raivo-otp/issuer-icons&typeValue2=master" /></a>
    <br/>
    <b>This repository contains icons (including build scripts) for issuers that can be used in Raivo OTP</b>
    <br/>
    <sup>Built by <a href="https://www.linkedin.com/in/tijme/">Tijme Gommers</a> – Buy me a coffee via <a href="https://www.paypal.me/tijmegommers">PayPal</a></sup>
    <br/>
</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/reddit/reddit-alien.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/bitbucket/bitbucket.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/google/google.svg?sanitize=true" width="75" /> 
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/whatsapp/whatsapp.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/amazon/amazon.svg?sanitize=true" width="75" /> 
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/atlassian/atlassian.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/spotify/spotify.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/slack/slack.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/facebook-messenger/facebook-messenger.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/gitlab/gitlab.svg?sanitize=true" width="75" />
</p>

# Contributing

The example below shows how icons can be added for the services "Microsoft" and "Microsoft OneDrive".

1. Create the directory with the primary domain name `./vectors/microsoft.com`.
2. Add a scalable Microsoft logo SVG (that meets the [requirements](#svg-requirements)) at `./vectors/microsoft.com/microsoft.svg`.
3. Add a scalable Microsoft OneDrive logo SVG (that meets the [requirements](#svg-requirements)) at `./vectors/microsoft.com/microsoft-onedrive.svg`.

# SVG requirements

**Must:**
* Must be a vector SVG
    * Do not convert JPG/PNG/etc to SVG
    * Do not embed JPG/PNG/etc in the SVG
* Must be a (somewhat) square icon. 
    * Prevent the use of textual icons.
* Must start with the `<svg>` opening element
* Must end with the `</svg>` closing element
* Must be scalable (must not have static width/height attributes, use a viewBox instead).
* Must not contain whitespace around the SVG ([this](https://jsfiddle.net/0mLp9vgk/) JSFiddle could help to remove whitespace).
* Must not include the doctype element.
* The file and directory name must be lowercase without spaces (use dashes instead)

**Can:**
* Can be any color (including white and black).
    * Raivo OTP will apply effects so the icons are correctly visible in light/dark mode.

For best practice examples, check the SVG of e.g. [Amazon](https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/amazon/amazon.svg), [Adobe](https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/adobe/adobe.svg) or [Bitbucket](https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/bitbucket/bitbucket.svg). Pull requests that do not meet the requirements will not be merged.
