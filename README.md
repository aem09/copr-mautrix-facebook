[![Copr build status](https://copr.fedorainfracloud.org/coprs/aem/matrix/package/mautrix-facebook/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/aem/matrix/package/mautrix-facebook/)

## Setup

1. Activate COPR Repo.
1. Install mautrix-facebook
1. Configure as required in /etc/mautrix/facebook/config.yaml
1. Generate registaration using python -m mautrix_facebook -g -c /etc/mautrix/facebook/config.yaml -r /etc/mautrix/facebook/registration.yaml
1. Add registration yaml to synapse.
1. Run the bridge with systemctl start mautrix-facebook
1. Use systemctl enable to start on boot if required.
