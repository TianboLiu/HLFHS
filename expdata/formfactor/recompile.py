import numpy as np
import pandas as pd
import os, sys

Mp = 0.938272081
Mn = 0.939565413
mup = 2.7928473446
mun = -1.9130427

def fm2GeV(var, power):
    hbar = 0.1973269788
    return var * hbar ** power

def G_D(Q2):
    return np.power(1.0 + Q2/0.71, -2)

def Load(idx):
    name = '{:0>4d}.dat'.format(idx)
    d0 = pd.read_table(name, delim_whitespace=True, skiprows=8, header=[0,1])
    # mu*G_Ep/G_Mp
    if idx in [1,2,3,4,5,6,46,51,52,53,54,55]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['mu*G_Ep/G_Mp'] = d0['mu*G_Ep/G_Mp'].values.flatten()
        d1['error'] = ((d0['err_stat']**2+d0['err_syst']**2)**0.5).values.flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [16]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['mu*G_Ep/G_Mp'] = d0['mu*G_Ep/G_Mp'].values.flatten()
        d1['error'] = ((d0['err_stat'].values**2+(d0['mu*G_Ep/G_Mp'].values*d0['err_syst'].values/100.0)**2)**0.5).flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [11,12,17]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['mu*G_Ep/G_Mp'] = (d0['(mu*G_Ep/G_Mp)^2']**0.5).values.flatten()
        d1['error'] = ((d0['(mu*G_Ep/G_Mp)^2'].values + d0['err_total'].values)**0.5).flatten() - d1['mu*G_Ep/G_Mp']
        d2 = pd.DataFrame(data=d1)
    elif idx in [31,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['mu*G_Ep/G_Mp'] = d0['mu*G_Ep/G_Mp'].values.flatten()
        d1['error'] = (d0['err_total+'].values/2 - d0['err_total-'].values/2).flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [37,40]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['mu*G_Ep/G_Mp'] = d0['mu*G_Ep/G_Mp'].values.flatten()
        d1['error'] = d0['err_total'].values.flatten()
        d2 = pd.DataFrame(data=d1)
    # G_Ep/G_D 
    elif idx in [7,14,21]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Ep/G_D'] = d0['G_Ep'].values.flatten() / G_D(d1['Q2'])
        d1['error'] = ((d0['err_stat'].values**2 + (d0['G_Ep'].values*d0['err_syst'].values/100.0)**2)**0.5).flatten() / G_D(d1['Q2'])
        d2 = pd.DataFrame(data=d1)
    elif idx in [23,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Ep/G_D'] = d0['G_Ep'].values.flatten() / G_D(d1['Q2'])
        d1['error'] = ((d0['err_stat'].values**2 + d0['err_syst'].values**2)**0.5).flatten() * d1['G_Ep/G_D']
        d2 = pd.DataFrame(data=d1)
    elif idx in [76,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Ep/G_D'] = d0['G_Ep'].values.flatten() / G_D(d1['Q2'])
        d1['error'] = d0['err_total'].values.flatten() / G_D(d1['Q2'])
        d2 = pd.DataFrame(data=d1)
    elif idx in [26,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Ep/G_D'] = d0['G_Ep/G_D'].values.flatten()
        d1['error'] = ((d0['err_stat'].values**2 + d0['err_syst'].values**2 + d0['err_norm'].values**2)**0.5).flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [29,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Ep/G_D'] = d0['G_Ep/G_D'].values.flatten()
        d1['error'] = (((d0['err_total+'].values/2 - d0['err_total-'].values/2)**2 + (d0['G_Ep/G_D'].values*d0['err_norm'].values/100.0)**2)**0.5).flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [35,38]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Ep/G_D'] = d0['G_Ep/G_D'].values.flatten()
        d1['error'] = d0['err_total'].values.flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [9,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Ep/G_D'] = (d0['G_Ep^2']**0.5).values.flatten() / G_D(d1['Q2'])
        d1['error'] = ((d0['G_Ep^2'].values + d0['err_total'].values)**0.5).flatten() / G_D(d1['Q2']) - d1['G_Ep/G_D']
        d2 = pd.DataFrame(data=d1)
    # G_Mp/mu/G_D
    elif idx in [8,15,22]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mp/mu/G_D'] = d0['G_Mp/mu'].values.flatten() / G_D(d1['Q2'])
        d1['error'] = ((d0['err_stat'].values**2 + (d0['G_Mp/mu'].values*d0['err_syst'].values/100.0)**2)**0.5).flatten() / G_D(d1['Q2'])
        d2 = pd.DataFrame(data=d1)
    elif idx in [27,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mp/mu/G_D'] = d0['G_Mp/mu/G_D'].values.flatten()
        d1['error'] = ((d0['err_stat'].values**2 + d0['err_syst'].values**2 + d0['err_norm'].values**2)**0.5).flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [30,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mp/mu/G_D'] = d0['G_Mp/mu/G_D'].values.flatten()
        d1['error'] = (((d0['err_total+'].values/2 - d0['err_total-'].values/2)**2 + (d0['G_Mp/mu/G_D'].values*d0['err_norm'].values/100.0)**2)**0.5).flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [36,39]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mp/mu/G_D'] = d0['G_Mp/mu/G_D'].values.flatten()
        d1['error'] = d0['err_total'].values.flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [13,18]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mp/mu/G_D'] = d0['G_Mp'].values.flatten() / G_D(d1['Q2']) / mup
        d1['error'] = d0['err_total'].values.flatten() / 100.0 * d1['G_Mp/mu/G_D']
        d2 = pd.DataFrame(data=d1)
    elif idx in [10,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mp/mu/G_D'] = (d0['G_Mp^2']**0.5).values.flatten() / G_D(d1['Q2']) / mup
        d1['error'] = ((d0['G_Mp^2'].values + d0['err_total'].values)**0.5).flatten() / G_D(d1['Q2']) / mup - d1['G_Mp/mu/G_D']
        d2 = pd.DataFrame(data=d1)
    elif idx in [24,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mp/mu/G_D'] = d0['Q^4*G_Mp/mu'].values.flatten() / d1['Q2']**2 / G_D(d1['Q2'])
        d1['error'] = ((d0['err_stat'].values**2 + d0['err_syst'].values**2)**0.5).flatten() / d1['Q2']**2 / G_D(d1['Q2'])
        d2 = pd.DataFrame(data=d1)
    # mu*G_En/G_Mn
    elif idx in [57,74]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['mu*G_En/G_Mn'] = d0['mu*G_En/G_Mn'].values.flatten()
        d1['error'] = ((d0['err_stat']**2+d0['err_syst']**2)**0.5).values.flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [60,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['mu*G_En/G_Mn'] = d0['G_En/G_Mn'].values.flatten() * mun
        d1['error'] = ((d0['err_stat']**2 + d0['err_syst']**2)**0.5).values.flatten() * np.abs(mun)
        d2 = pd.DataFrame(data=d1)
    # G_En
    elif idx in [41,42,43,44,45,47,49,59,61,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_En'] = d0['G_En'].values.flatten()
        d1['error'] = ((d0['err_stat']**2 + d0['err_syst']**2)**0.5).values.flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [48,50,58]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_En'] = d0['G_En'].values.flatten()
        d1['error'] = ((d0['err_stat']**2 + (d0['err_syst+']/2 - d0['err_syst-']/2)**2)**0.5).values.flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [56,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_En'] = d0['G_En'].values.flatten()
        d1['error'] = d0['err_total'].values.flatten()
        d2 = pd.DataFrame(data=d1)
    # G_Mn/mu/G_D
    elif idx in [20,63,64,68]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mn/mu/G_D'] = d0['G_Mn/mu/G_D'].values.flatten()
        d1['error'] = d0['err_total'].values.flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [62,65,70]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mn/mu/G_D'] = d0['G_Mn/mu/G_D'].values.flatten()
        d1['error'] = ((d0['err_stat']**2 + d0['err_syst']**2)**0.5).values.flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [72,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mn/mu/G_D'] = d0['G_Mn/mu/G_D'].values.flatten()
        d1['error'] = ((d0['err_stat']**2 + d0['err_syst']**2 + d0['err_model']**2)**0.5).values.flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [69,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mn/mu/G_D'] = d0['G_Mn/mu/G_D'].values.flatten()
        d1['error'] = ((d0['err_stat'].values**2 + (d0['G_Mn/mu/G_D'].values*d0['err_syst'].values/100.0)**2)**0.5).flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [66,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mn/mu/G_D'] = d0['(G_Mn/mu/G_D)^2'].values.flatten()**0.5
        d1['error'] = ((d0['(G_Mn/mu/G_D)^2'] + (d0['err_stat']**2 + d0['err_syst']**2)**0.5)**0.5).values.flatten() - d1['G_Mn/mu/G_D']
        d2 = pd.DataFrame(data=d1)
    elif idx in [67,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mn/mu/G_D'] = d0['G_Mn/mu/G_D'].values.flatten()
        d1['error'] = ((d0['err_stat']**2 + d0['err_syst']**2 + d0['err_model']**2)**0.5/100.0).values.flatten() * d1['G_Mn/mu/G_D']
        d2 = pd.DataFrame(data=d1)
    elif idx in [73,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['G_Mn/mu/G_D'] = d0['G_Mn'].values.flatten() / G_D(d1['Q2']) / mun
        d1['error'] = d0['err_total'].values.flatten() / G_D(d1['Q2']) / np.abs(mun)
        d2 = pd.DataFrame(data=d1)
    # Q^4*F_1p
    elif idx in [25,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['Q^4*F_1p'] = d0['Q^4*F_1p'].values.flatten()
        d1['error'] = ((d0['err_stat'].values**2 + d0['err_syst'].values**2)**0.5).flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [32,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['Q^4*F_1p'] = d0['F_1p/G_D'].values.flatten() * G_D(d1['Q2']) * d1['Q2']**2
        d1['error'] = ((d0['err_total+'].values.flatten()/2 - d0['err_total-'].values.flatten()/2)**2 + (d1['Q^4*F_1p']*d0['err_norm'].values.flatten()/100.0)**2)**0.5
        d2 = pd.DataFrame(data=d1)
    # Q^2*F_2p/F_1p
    elif idx in [28,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['Q^2*F_2p/F_1p'] = d0['Q^2*F_2p/F_1p'].values.flatten()
        d1['error'] = ((d0['err_stat'].values**2 + d0['err_syst'].values**2 + d0['err_norm'].values**2)**0.5).flatten()
        d2 = pd.DataFrame(data=d1)
    elif idx in [34,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['Q^2*F_2p/F_1p'] = d0['Q^2*F_2p/F_1p'].values.flatten()
        d1['error'] = (d0['err_total+'].values - d0['err_total-'].values).flatten()/2
        d2 = pd.DataFrame(data=d1)
    # F_2p/G_D
    elif idx in [33,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        d1['F_2p/G_D'] = d0['F_2p/G_D'].values.flatten()
        d1['error'] = ((d0['err_total+'].values.flatten()/2 - d0['err_total-'].values.flatten()/2)**2 + (d1['F_2p/G_D'] * d0['err_norm'].values.flatten()/100.0)**2)**0.5
        d2 = pd.DataFrame(data=d1)        
    # sigma/sigma_D
    elif idx in [75,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        Eb = d0['E_beam'].values.flatten()
        d1['epsilon'] = 1.0 / (1.0 + 2.0 * (1.0 + d1['Q2']/(4.0 * Mp * Mp)) * d1['Q2'] / (4.0 * Eb * (Eb - d1['Q2']/(2.0 * Mp)) - d1['Q2']))
        d1['sigma/sigma_D'] = d0['sigma/sigma_D'].values.flatten()
        d1['error'] = (d0['err_stat'].values.flatten()**2 + ((d0['err_syst'].values.flatten()-1.0) * d1['sigma/sigma_D'])**2)**0.5
        d2 = pd.DataFrame(data=d1)
    elif idx in [77,]:
        d1 = {}
        d1['Q2'] = d0['Q2'].values.flatten()
        if d0['Q2'].columns[0] == 'fm^-2': 
            d1['Q2'] = fm2GeV(d1['Q2'], 2)
        Eb = d0['E_beam'].values.flatten()
        d1['epsilon'] = 1.0 / (1.0 + 2.0 * (1.0 + d1['Q2']/(4.0 * Mp * Mp)) * d1['Q2'] / (4.0 * Eb * (Eb - d1['Q2']/(2.0 * Mp)) - d1['Q2']))
        d1['sigma/sigma_D'] = d0['sigma/sigma_D'].values.flatten()
        d1['error'] = (d0['err_stat'].values.flatten()**2 + (d0['err_syst'].values.flatten()/100.0 * d1['sigma/sigma_D'])**2)**0.5
        d2 = pd.DataFrame(data=d1)
    return d2

def Save(data, name):
    data.to_csv(name, sep='\t', index=False)
    print name, "saved"
    return
