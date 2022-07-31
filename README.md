<p align="center">
    <img src="https://raw.githubusercontent.com/raivo-otp/ios-application/master/Assets/app-icon.png" width="200"/>
</p>
<h1 align="center">Raivo OTP issuer icons</h1>
<p align="center">
    <a href="https://github.com/raivo-otp/ios-application/blob/master/LICENSE.md"><img src="https://raw.finnwea.com/shield/?firstText=License&secondText=CC%20BY-NC%204.0" /></a>
    <a href="https://travis-ci.org/raivo-otp/issuer-icons"><img src="https://raw.finnwea.com/vector-shields-v1/?typeKey=TravisBuildStatus&typeValue1=raivo-otp/issuer-icons&typeValue2=master" /></a>
    <a href="https://github.com/raivo-otp/issuer-icons/releases"><img src="https://raw.finnwea.com/vector-shields-v1/?typeKey=SemverVersion&typeValue1=raivo-otp&typeValue2=issuer-icons&typeValue4=Release&cache=4"></a>
    <br/>
    <b>This repository contains icons (including build scripts) for issuers that can be used in Raivo OTP</b>
    <br/>
    <sup>Raivo OTP is built by <a href="https://www.linkedin.com/in/tijme/">Tijme Gommers</a> – Buy me a coffee via <a href="https://www.paypal.me/tijmegommers">PayPal</a></sup>
    <br/>
</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/reddit.com/reddit.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/bitbucket.com/bitbucket.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/google.com/google.svg?sanitize=true" width="75" /> 
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/whatsapp.com/whatsapp.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/amazon.com/amazon.svg?sanitize=true" width="75" /> 
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/atlassian.com/atlassian.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/spotify.com/spotify.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/slack.com/slack.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/facebook.com/facebook-messenger.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/gitlab.com/gitlab.svg?sanitize=true" width="75" />
</p>

## Contributing

The example below shows how icons can be added for the services "Microsoft" and "Microsoft OneDrive".

1. Create the directory with the primary domain name `./vectors/microsoft.com`.
2. Add a scalable Microsoft logo SVG (that meets the [requirements](#svg-requirements)) at `./vectors/microsoft.com/microsoft.svg`.
3. Add a scalable Microsoft OneDrive logo SVG (that meets the [requirements](#svg-requirements)) at `./vectors/microsoft.com/microsoft-onedrive.svg`.

### SVG requirements

**Must:**
* Must be a vector SVG
    * Do not convert JPG/PNG/etc to SVG
    * Do not embed JPG/PNG/etc in the SVG
* Must be a (somewhat) square icon. 
    * Prevent the use of textual icons.
* Must start with the `<svg>` opening element
* Must end with the `</svg>` closing element
* Must be scalable (must not have static width/height attributes, use a viewBox instead).
* Must **not** contain whitespace around the SVG ([this](https://jsfiddle.net/u9x423ph/2/) JSFiddle could help to remove whitespace).
* Must **not** include the doctype element.
* The file and directory name must be lowercase.

**Can:**
* Can be any color (including white and black).
    * Raivo OTP will apply effects so the icons are correctly visible in light/dark mode.

For best practice examples, check the SVG of e.g. [Amazon](https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/amazon.com/amazon.svg), [Adobe](https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/adobe.com/adobe.svg) or [Bitbucket](https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/bitbucket.com/bitbucket.svg). Pull requests that do not meet the requirements will not be merged.

## Security

If you discover a security vulnerability, we would like to know about it so we can take steps to address it as quickly as possible. Please refer to the [security policy](https://github.com/raivo-otp/issuer-icons/blob/master/SECURITY.md) for information on reporting vulnerabilities.

## Privacy

Raivo does not collect personally identifiable information in any way. Please refer to the [privacy policy](https://github.com/raivo-otp/issuer-icons/blob/master/PRIVACY.md) for information.

## License

Copyright © 2022 Tijme Gommers. All rights reserved. View [LICENSE.md](https://github.com/raivo-otp/issuer-icons/blob/master/LICENSE.md) for the full license.
