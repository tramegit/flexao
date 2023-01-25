import streamlit as st
import iom
import concreto as ca

st.title('Flexão Simples de Seção Retangular')
st.markdown('## Concretos dos **Grupos I e II**.')

cola, colb = st.columns(2)
with cola:
	st.markdown("Seção Retangular")
	st.image("secao.png")	
with colb:
	fck = st.slider('Classe de Resistência do Concreto (MPa)', 5, 90, 25)		
	if fck <= 50:
		st.markdown('**Concreto do Grupo I**')
	else:
		st.markdown('**Concreto do Grupo II**')

	fcd = fck/1.40

	st.markdown('**Resistência de cálculo à compressão**')
	st.write('fcd =', iom.rd2(fcd), ' kN/cm²')  
	st.markdown('---')
	st.markdown('**Momento Fletor Solicitante de Cálculo**')
	md = st.number_input(' Md (kN.cm)', value = 1000.00 	, min_value = 1.0, step=0.01)

st.markdown('---')
# Inserindo os dados da seção e altura útil
col1, col2, col3 = st.columns(3)

with col1:
	bw = st.number_input('Base da Seção  bw(cm)', value = 19.00, min_value = 5.0, step=0.01) 

with col2:
	d = st.number_input('Altura últil da Seção  h(cm)', value = 26.50, min_value = 1.0, step=0.01)
	
with col3:
    aco = st.radio(
    "Tipo de aço",
    ('CA50', 'CA60', 'CA25'), index=0)	
    if aco == 'CA50':
              fyk = 500
    elif aco == 'CA60':
	      fyk = 600
    elif aco == 'CA25':
	      fyk = 250



if md > 0 and bw > 0 and d > 0 and fck > 0 and fyk > 0 :
	res = ca.flexosr(md, bw, d, fck, fyk) 
	
	st.markdown('## Resultados do Dimensionamento')
	col1, col2 = st.columns(2)
	with col1:
		st.write('Linha Neutra x (cm) : ', iom.rd2(res[2],4)) 
		st.write('Deformação Específica do Aço : ', iom.rd2(res[3],6)) 
	with col2:
		st.write('Relação x/d : ', iom.rd2(res[2]/d,4)) 
		st.write('x/d Limite : ', iom.rd2(res[4],6))

if 	(res[2]/d) <=  res[4] :
	st.metric(label="Área de Aço", value=iom.rd2(res[0],4), delta="cm²", delta_color="normal")
else:
	# st.success('Resultados do Dimensionamento', icon="✅")	
	st.warning('x/d acima do limite entre os domínios 3 e 4.', icon="⚠️")	
 
st.markdown('---')
st.markdown('Copyright (c) 2023 - Eng. Paulo C. Ormonde')

