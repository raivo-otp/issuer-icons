<p align="center">
    <img src="https://raw.githubusercontent.com/raivo-otp/ios-application/master/Assets/app-icon.png" width="200"/>
</p>
<h1 align="center">Raivo OTP issuer icons</h1>
<p align="center">
    <a href="https://github.com/raivo-otp/issuer-icons/blob/master/LICENSE.md"><img src="https://raw.finnwea.com/shield/?firstText=Source&secondText=Licensed" /></a>
    <a href="https://travis-ci.org/raivo-otp/issuer-icons"><img src="https://raw.finnwea.com/vector-shields-v1/?typeKey=TravisBuildStatus&typeValue1=raivo-otp/issuer-icons&typeValue2=master" /></a>
    <a href="https://github.com/raivo-otp/issuer-icons/releases"><img src="https://raw.finnwea.com/vector-shields-v1/?typeKey=SemverVersion&typeValue1=raivo-otp&typeValue2=issuer-icons&typeValue4=Release&cache=4"></a>
    <br/>
    <b>Vector icons (including test, build and deployment scripts) for one-time password issuers used in Raivo OTP</b>
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

### Requirements

If you want to contribute and add an issuer icon, make sure it adheres to the following requirements. Pull requests failing to meet these requirements will not be merged.

**Must:**
* Must be a vector SVG
    * Do not convert JPG/PNG/etc to SVG
    * Do not embed JPG/PNG/etc in the SVG
* Must be a (somewhat) square icon. 
    * Prevent the use of textual icons.
* Must be the original brand logo, not that from an icon pack.
* Must start with the `<svg>` opening element
* Must end with the `</svg>` closing element
* Must be scalable (must not have static width/height attributes, use a viewBox instead).
* Must **not** contain whitespace around the SVG ([this](https://jsfiddle.net/u9x423ph/2/) JSFiddle could help to remove whitespace).
* Must **not** include the doctype element.
* The file and directory name must be lowercase.
* Must be in the `vectors/` directory.

**Can:**
* Can be any color (including white and black).
    * Raivo OTP will apply effects so the icons are correctly visible in light/dark mode.

You may run the validation script before contributing a pull request to double check if your icon meets the requirements:

    python scripts/validate.py

For best practice examples, check the SVG of e.g. [Amazon](https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/amazon.com/amazon.svg), [Adobe](https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/adobe.com/adobe.svg) or [Bitbucket](https://raw.githubusercontent.com/raivo-otp/issuer-icons/master/vectors/bitbucket.com/bitbucket.svg).

## Security

If you discover a security vulnerability, we would like to know about it so we can take steps to address it as quickly as possible. Please report your vulnerability via our [HackerOne](https://hackerone.com/raivo) program. If you want to know more about how we keep Raivo OTP secure, check out the [security policy](https://github.com/raivo-otp/issuer-icons/blob/master/SECURITY.md).

## Privacy

Raivo does not collect personally identifiable information in any way. Please refer to the [privacy policy](https://github.com/raivo-otp/issuer-icons/blob/master/PRIVACY.md) for information.

## License

The source of Raivo OTP is copyrighted but available to anyone on the internet. You can use it in accordence of the license. View [LICENSE.md](https://github.com/raivo-otp/issuer-icons/blob/master/LICENSE.md) for the full license.
