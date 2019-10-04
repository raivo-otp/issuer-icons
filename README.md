<p align="center">
    <img src="https://raw.githubusercontent.com/tijme/raivo/master/Assets/app-icon.png" width="200"/>
</p>
<h1 align="center">Raivo OTP issuer icons</h1>
<p align="center">
    <a href="https://github.com/tijme/raivo/blob/master/LICENSE.md"><img src="https://raw.finnwea.com/shield/?firstText=License&secondText=CC%20BY-NC%204.0" /></a>
    <a href="https://travis-ci.org/tijme/raivo-issuer-icons"><img src="https://raw.finnwea.com/shield/?typeKey=TravisBuildStatus&typeValue1=tijme/raivo-issuer-icons&typeValue2=master" /></a>
    <br/>
    <b>This repository contains icons (including build scripts) for issuers that can be used in Raivo OTP</b>
    <br/>
    <sup>Built by <a href="https://www.linkedin.com/in/tijme/">Tijme Gommers</a> – Buy me a coffee via <a href="https://www.paypal.me/tijmegommers">PayPal</a></sup>
    <br/>
</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/reddit/reddit-alien.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/bitbucket/bitbucket.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/google/google.svg?sanitize=true" width="75" /> 
    <img src="https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/whatsapp/whatsapp.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/amazon/amazon.svg?sanitize=true" width="75" /> 
    <img src="https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/atlassian/atlassian.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/spotify/spotify.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/slack/slack.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/facebook-messenger/facebook-messenger.svg?sanitize=true" width="75" />
    <img src="https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/gitlab/gitlab.svg?sanitize=true" width="75" />
</p>

# Contributing

The example below shows how an icon can be added for the service "Twitter".

1. Create the directory `./vectors/twitter`.
2. Add a scalable SVG (that meets the [requirements](#svg-requirements)) at `./vectors/twitter/twitter.svg`.
3. Add `./vectors/twitter/information.json` to the directory with [this](https://github.com/tijme/raivo-issuer-icons/blob/master/vectors/twitter/information.json) content. Additionally, [search terms](https://github.com/tijme/raivo-issuer-icons/blob/master/vectors/microsoft-outlook/information.json) can be added.

# SVG requirements

* must be scalable
* must not include the doctype element
* must start with the `<svg>` opening element
* must end with the `</svg>` closing element
* recommended to be square

For examples, check the SVG of e.g. [Amazon](https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/amazon/amazon.svg), [Adobe](https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/adobe/adobe.svg) or [Bitbucket](https://raw.githubusercontent.com/tijme/raivo-issuer-icons/master/vectors/bitbucket/bitbucket.svg).
