import pandas as pd
import sys

if len(sys.argv) != 2:
    print("\n\nNumero de argumento errado\n\n")
    sys.exit(1)

planilha = pd.read_excel(f'{sys.argv[1]}.xlsx')

arquivo = open("pjsip_additional.txt", "w")
print(range(planilha.shape[0]))
for i in range(planilha.shape[0]):
    ramal = planilha.loc[i, "username"]
    call_group = planilha.loc[i, "call group"]
    pick_group = planilha.loc[i, "pick group"]
    display = planilha.loc[i, "display"]
    password = planilha.loc[i, "password"]
    contexto = planilha.loc[i, "contexto"]

    padrao = f'''
[{ramal}]
auth=auth{ramal}
aors={ramal}
type=endpoint
language=pt_BR
deny=0.0.0.0/0.0.0.0
disallow=all
ext={contexto}
trust_id_inbound=yes
send_rpid=no
transport=transport-udp
rtcp_mux=no
call_group={call_group}
pickup_group={pick_group}
allow=ulaw,alaw,h264,h263
mailboxes=1001@default
permit=0.0.0.0/0.0.0.0
ice_support=no
use_avpf=no
dtls_cert_file=
dtls_private_key=
dtls_ca_file=
dtls_setup=actpass
dtls_verify=no
media_encryption=no
message_context=mensagens_texto
subscribe_context=
allow_subscribe=yes
stir_shaken=off
rtp_symmetric=yes
force_rport=yes
rewrite_contact=yes
direct_media=no
media_use_received_transport=no
callerid={display} <{ramal}>

[auth{ramal}]
type=auth
auth_type=userpass
username={ramal}
password={password}

[{ramal}]
type=aor
qualify_frequency=60
ax_contacts=1
remove_existing=no
qualify_timeout=3.0
authenticate_qualify=no'''
    arquivo.write(padrao + "\n")

arquivo.close()
print("\n\n------------FIM DO PROGRAMA---------------\n\n")
sys.exit(0)