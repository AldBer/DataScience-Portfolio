{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cbb9f49a-d376-4d83-bde3-6c899b36c02d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "bairro=%{x}<br>preco=%{y}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa",
          "pattern": {
           "shape": ""
          }
         },
         "name": "",
         "orientation": "v",
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Perdizes",
          "Jardins",
          "Lapa",
          "Itaim Bibi",
          "Perdizes",
          "Santo Amaro",
          "Vila Mariana",
          "Perdizes",
          "Lapa",
          "Itaim Bibi",
          "Jardins",
          "Lapa",
          "Lapa",
          "Vila Mariana",
          "Morumbi",
          "Itaim Bibi",
          "Moema",
          "Lapa",
          "Morumbi",
          "Moema",
          "Itaim Bibi",
          "Pinheiros",
          "Santo Amaro",
          "Morumbi",
          "Tatuapé",
          "Pinheiros",
          "Santo Amaro",
          "Vila Mariana",
          "Perdizes",
          "Jardins",
          "Tatuapé",
          "Vila Mariana",
          "Itaim Bibi",
          "Vila Mariana",
          "Perdizes",
          "Itaim Bibi",
          "Tatuapé",
          "Perdizes",
          "Moema",
          "Jardins",
          "Tatuapé",
          "Moema",
          "Santo Amaro",
          "Tatuapé",
          "Santo Amaro",
          "Itaim Bibi",
          "Moema",
          "Jardins",
          "Perdizes",
          "Lapa",
          "Vila Mariana",
          "Pinheiros",
          "Jardins",
          "Moema",
          "Lapa",
          "Jardins",
          "Moema",
          "Morumbi",
          "Morumbi",
          "Santo Amaro",
          "Jardins",
          "Morumbi",
          "Moema",
          "Santo Amaro",
          "Moema",
          "Santo Amaro",
          "Jardins",
          "Lapa",
          "Perdizes",
          "Tatuapé",
          "Lapa",
          "Itaim Bibi",
          "Moema",
          "Itaim Bibi",
          "Lapa",
          "Santo Amaro",
          "Tatuapé",
          "Tatuapé",
          "Pinheiros",
          "Tatuapé",
          "Perdizes",
          "Tatuapé",
          "Lapa",
          "Pinheiros",
          "Lapa",
          "Lapa",
          "Vila Mariana",
          "Pinheiros",
          "Lapa",
          "Vila Mariana",
          "Vila Mariana",
          "Pinheiros",
          "Itaim Bibi",
          "Santo Amaro",
          "Perdizes",
          "Santo Amaro",
          "Tatuapé",
          "Perdizes",
          "Tatuapé",
          "Lapa",
          "Moema",
          "Pinheiros",
          "Perdizes",
          "Perdizes",
          "Lapa",
          "Itaim Bibi",
          "Vila Mariana",
          "Lapa",
          "Morumbi",
          "Vila Mariana",
          "Pinheiros",
          "Vila Mariana",
          "Itaim Bibi",
          "Vila Mariana",
          "Pinheiros",
          "Itaim Bibi",
          "Santo Amaro",
          "Perdizes",
          "Perdizes",
          "Tatuapé",
          "Santo Amaro",
          "Santo Amaro",
          "Vila Mariana",
          "Perdizes",
          "Pinheiros",
          "Jardins",
          "Jardins",
          "Itaim Bibi",
          "Perdizes",
          "Perdizes",
          "Jardins",
          "Perdizes",
          "Vila Mariana",
          "Morumbi",
          "Moema",
          "Santo Amaro",
          "Tatuapé",
          "Itaim Bibi",
          "Morumbi",
          "Jardins",
          "Santo Amaro",
          "Perdizes",
          "Tatuapé",
          "Perdizes",
          "Pinheiros",
          "Pinheiros",
          "Tatuapé",
          "Tatuapé",
          "Jardins",
          "Tatuapé",
          "Vila Mariana",
          "Perdizes",
          "Morumbi",
          "Lapa",
          "Tatuapé",
          "Itaim Bibi",
          "Pinheiros",
          "Vila Mariana",
          "Santo Amaro",
          "Lapa",
          "Morumbi",
          "Lapa",
          "Tatuapé",
          "Jardins",
          "Pinheiros",
          "Pinheiros",
          "Santo Amaro",
          "Jardins",
          "Perdizes",
          "Moema",
          "Vila Mariana",
          "Pinheiros",
          "Itaim Bibi",
          "Pinheiros",
          "Lapa",
          "Pinheiros",
          "Pinheiros",
          "Moema",
          "Moema",
          "Morumbi",
          "Perdizes",
          "Itaim Bibi",
          "Pinheiros",
          "Pinheiros",
          "Vila Mariana",
          "Moema",
          "Itaim Bibi",
          "Santo Amaro",
          "Morumbi",
          "Perdizes",
          "Jardins",
          "Perdizes",
          "Lapa",
          "Pinheiros",
          "Morumbi",
          "Lapa",
          "Itaim Bibi",
          "Jardins",
          "Moema",
          "Morumbi",
          "Morumbi",
          "Pinheiros",
          "Tatuapé",
          "Morumbi",
          "Vila Mariana",
          "Jardins",
          "Jardins",
          "Vila Mariana",
          "Santo Amaro",
          "Vila Mariana",
          "Vila Mariana",
          "Jardins",
          "Perdizes",
          "Jardins",
          "Tatuapé",
          "Pinheiros",
          "Lapa",
          "Perdizes",
          "Moema",
          "Lapa",
          "Pinheiros",
          "Tatuapé",
          "Tatuapé",
          "Moema",
          "Perdizes",
          "Santo Amaro",
          "Vila Mariana",
          "Perdizes",
          "Santo Amaro",
          "Tatuapé",
          "Jardins",
          "Pinheiros",
          "Moema",
          "Pinheiros",
          "Itaim Bibi",
          "Itaim Bibi",
          "Perdizes",
          "Tatuapé",
          "Tatuapé",
          "Vila Mariana",
          "Vila Mariana",
          "Vila Mariana",
          "Jardins",
          "Lapa",
          "Morumbi",
          "Lapa",
          "Pinheiros",
          "Lapa",
          "Jardins",
          "Pinheiros",
          "Lapa",
          "Jardins",
          "Morumbi",
          "Lapa",
          "Jardins",
          "Vila Mariana",
          "Tatuapé",
          "Vila Mariana",
          "Tatuapé",
          "Moema",
          "Moema",
          "Moema",
          "Morumbi",
          "Vila Mariana",
          "Tatuapé",
          "Jardins",
          "Pinheiros",
          "Jardins",
          "Pinheiros",
          "Itaim Bibi",
          "Jardins",
          "Lapa",
          "Lapa",
          "Perdizes",
          "Vila Mariana",
          "Pinheiros",
          "Pinheiros",
          "Vila Mariana",
          "Morumbi",
          "Perdizes",
          "Morumbi",
          "Morumbi",
          "Morumbi",
          "Vila Mariana",
          "Morumbi",
          "Lapa",
          "Moema",
          "Itaim Bibi",
          "Pinheiros",
          "Pinheiros",
          "Itaim Bibi",
          "Vila Mariana",
          "Jardins",
          "Vila Mariana",
          "Pinheiros",
          "Pinheiros",
          "Itaim Bibi",
          "Morumbi",
          "Vila Mariana",
          "Tatuapé",
          "Itaim Bibi",
          "Lapa",
          "Pinheiros",
          "Itaim Bibi",
          "Vila Mariana",
          "Pinheiros",
          "Jardins",
          "Itaim Bibi",
          "Perdizes",
          "Pinheiros",
          "Vila Mariana",
          "Moema",
          "Tatuapé",
          "Santo Amaro",
          "Morumbi",
          "Santo Amaro",
          "Vila Mariana",
          "Lapa",
          "Lapa",
          "Moema",
          "Morumbi",
          "Perdizes",
          "Moema",
          "Santo Amaro",
          "Moema",
          "Santo Amaro",
          "Pinheiros",
          "Lapa",
          "Pinheiros",
          "Tatuapé",
          "Morumbi",
          "Perdizes",
          "Santo Amaro",
          "Perdizes",
          "Santo Amaro",
          "Vila Mariana",
          "Moema",
          "Tatuapé",
          "Lapa",
          "Santo Amaro",
          "Perdizes",
          "Tatuapé",
          "Jardins",
          "Jardins",
          "Pinheiros",
          "Lapa",
          "Vila Mariana",
          "Perdizes",
          "Moema",
          "Moema",
          "Perdizes",
          "Morumbi",
          "Vila Mariana",
          "Tatuapé",
          "Santo Amaro",
          "Morumbi",
          "Santo Amaro",
          "Santo Amaro",
          "Morumbi",
          "Pinheiros",
          "Jardins",
          "Santo Amaro",
          "Morumbi",
          "Morumbi",
          "Itaim Bibi",
          "Pinheiros",
          "Lapa",
          "Itaim Bibi",
          "Itaim Bibi",
          "Perdizes",
          "Jardins",
          "Morumbi",
          "Jardins",
          "Vila Mariana",
          "Perdizes",
          "Lapa",
          "Jardins",
          "Moema",
          "Santo Amaro",
          "Vila Mariana",
          "Pinheiros",
          "Lapa",
          "Vila Mariana",
          "Santo Amaro",
          "Perdizes",
          "Santo Amaro",
          "Itaim Bibi",
          "Santo Amaro",
          "Itaim Bibi",
          "Perdizes",
          "Tatuapé",
          "Itaim Bibi",
          "Pinheiros",
          "Santo Amaro",
          "Santo Amaro",
          "Pinheiros",
          "Moema",
          "Morumbi",
          "Tatuapé",
          "Lapa",
          "Itaim Bibi",
          "Pinheiros",
          "Perdizes",
          "Itaim Bibi",
          "Morumbi",
          "Perdizes",
          "Vila Mariana",
          "Santo Amaro",
          "Vila Mariana",
          "Itaim Bibi",
          "Morumbi",
          "Tatuapé",
          "Itaim Bibi",
          "Pinheiros",
          "Jardins",
          "Itaim Bibi",
          "Santo Amaro",
          "Santo Amaro",
          "Itaim Bibi",
          "Perdizes",
          "Jardins",
          "Pinheiros",
          "Itaim Bibi",
          "Perdizes",
          "Santo Amaro",
          "Santo Amaro",
          "Morumbi",
          "Itaim Bibi",
          "Jardins",
          "Moema",
          "Jardins",
          "Santo Amaro",
          "Santo Amaro",
          "Vila Mariana",
          "Santo Amaro",
          "Pinheiros",
          "Lapa",
          "Itaim Bibi",
          "Jardins",
          "Lapa",
          "Perdizes",
          "Moema",
          "Pinheiros",
          "Jardins",
          "Lapa",
          "Moema",
          "Vila Mariana",
          "Pinheiros",
          "Pinheiros",
          "Vila Mariana",
          "Itaim Bibi",
          "Vila Mariana",
          "Pinheiros",
          "Pinheiros",
          "Lapa",
          "Santo Amaro",
          "Moema",
          "Vila Mariana",
          "Moema",
          "Vila Mariana",
          "Perdizes",
          "Pinheiros",
          "Santo Amaro",
          "Lapa",
          "Santo Amaro",
          "Santo Amaro",
          "Santo Amaro",
          "Moema",
          "Vila Mariana",
          "Tatuapé",
          "Perdizes",
          "Jardins",
          "Santo Amaro",
          "Itaim Bibi",
          "Moema",
          "Lapa",
          "Jardins",
          "Tatuapé",
          "Itaim Bibi",
          "Tatuapé",
          "Jardins",
          "Santo Amaro",
          "Itaim Bibi",
          "Tatuapé",
          "Lapa",
          "Vila Mariana",
          "Pinheiros",
          "Vila Mariana",
          "Jardins",
          "Moema",
          "Pinheiros",
          "Perdizes",
          "Lapa",
          "Perdizes",
          "Itaim Bibi",
          "Pinheiros",
          "Perdizes",
          "Perdizes",
          "Tatuapé",
          "Vila Mariana"
         ],
         "xaxis": "x",
         "y": {
          "bdata": "2QgMALbPCAATIggAawgSAL9lCQCmShcAfboFAEkGFwCJORAA6tAOAKzDDAD9FREAJhYPAC9PFAAcyA8AY/IPACSYDQCE/w4A9aoQACVuBwBYFgkAQ6kSAHwKEAClag4A2lcPAJPZEAC4yQwALbILAMInEAC4xwoArCARAAl3BwBL+BMAE2wRAEluEADXwRMA+uEWAPfmEwD61AYAv2YJAApmDADTYA8A4qARAMXvCwAeHRAACc0LAKF1DADS0QgAVggLAD8SCQCmygoA/RQUAKzpCgATTxsAW4QRANsaEABdVAsA7XYSAK2fDAA70Q8AWfoaAK7RDgAOhRQANwoMAD8ZDwBoXRcAhmMMADeOFwCmfxIAHK8MAFonEgD2tRMA7xoSACUSCAAj7gsAMCAOAAbrDgCaGRIAfhIQAGUlCQDL/xAAyA0SAEHSEQDKNBQAgRMTAFpcEQAG8A4A0KcHALU5EQCiNRAAgoAQAA9qCQBjTwoAahQUAOUTDwDiYBIAcGMPAB9lDwDNjRMAg+UMAOSyDwCFJA0AE0UNAPDXDQCQRhAANxENANcBFQDiKQsAQ2cOAPE+DQDt4RUAligQAHH7EwBcdQgAM3sQAMlUEwCtog8A3CIUAA3kDADUtRUARcgZAAyZDQAtOA0Ab+kVAFB9FgCG3QwA2FUNAAn4DQC5GgkAtA0LAIapCgB9vgsAmxkPALhUEAA+WxYATrAKAMHDEwB7Rw4ASQgPAA5ZEgCPHgoAYwIRAFAFEABXgxEAH5UQAI5/GgDmVgwA/dMMAAJoDABNtwwAUFcMAKGzFADnwhUAaKUMANVyCwCxahEAHbsMAPgnEgANMBAA/VEIALxXFgDLehcAI3QMAOp7DQBAkRAAMcoQAPtFEgD1dRgA5HIOAL+aCwDc8QgAsekLAG4bDwA/eRcAreMMAIBIEAABLw8A5rIUAIDTGgAj1AwAsAQNAOAJFABXYRIAXLYXAIruEQA0nQ0AbPYRAINVFADBAxMAtpQRAEIkFACFnBQA+JUVAHU6EgBpfg4ALu4PACHIFADnhAsASvIQAE51DQDvYw8AcBwVADIiEACreA8AqwgJAMSsEgCtNhIAUCkZAJPZDQARQxAAf2YQANR6FgCT0g4AOokQAKEKEgDvHBAAFjcNALMlEABqLBQATY8KABPeDwDMDQwAsroUAERJCABDswwATPwQANlsFgAz9Q4AoLcMALveFwBcoQgAhjEFAORFEQDo9QwAfpUKAFuAEgD0XxAAOK0MAOVlCQCpQBMANDwSAAfODgBHthcAP1wKAIZGCABsFwwA1AwPAGpfEACNJw4A0d4QAJqHCQAp3hUA++EOAJVfFADi0xAAglkRAPLdEQDpThEAcTMSANpXFQCMKBAAHYESABfZDgDj2RUAmikMALqAFwAxEw8Aj7UIAF/YDwAlJAwAYRsTAHVFDABhNw0A8psGADQwDQDEKQQAHQIIAFy9EgAc2xIA1TQRABPVCgBXCg8ABz4PAMv0CQALJBYAaUYTAE8/DgDCYQ8AczYQAJjpBQCXIA4ADSMMAHqsCgDW+A0A6nwXAD0xEgDmpAwAP+ERAB+qFQDOfRMAIYgPAB9MDAB7dBIAXg8RAE5bEwCYKhIAMhAUAAXPDAASShUA0CkQADLCGACcGgwAlTQXAC0qEADfRgwAMgsNANjKDQBSMxEA86YRAPKhDAC2JQ8AuRAZALcqFwCRQREAyW4PAOnODwA3ERIAqpMKAKMUDgDhngcAFxYRAK84EgAEDA0AxHYWAM6lCQAwjggASEkQAFENFACa9xYAfygNAFQyFAAfFQ8A9HcOAMpNEwCxPhIA6goIAJIEFgCLkxUAK2UMABUSEQAxhREAunMQAFy9DAAxLwwATiQPAIugFABIvxEA8I8NAJbKEgAdOAIAdoQUAIZLBwCEmQ0AIyIKAAxVCQCYkhQAKh4NAE/YEABECw8ASHERAEecDwC+YgkAwNETAKH/DAAhIggAjUwNAPQgFgCbJhMArKkNAPeoDQBVyQ0A8MMYANUBEQA0OhEAnfkTABVaEACvEg4AJ1wOAFjuDgChFg8A8ZYSACB/DwDQnBIAqeMOAGeeDwCcHAYAEnQTAEvYEADL0xMAMwACAJDRGACrng4A51QUAJx/CgBYEBIAx28KAEVnDABBBRgAy2IOAA5BEADcPRMAIYcRAIbyDwDw7RAAwUIaALr+DgDqLRAAfBEUAMpRFABNsRQAwy4SAMsGCgBtvBYA4AIKAOekEABVzgsAFvcOAIXDEADXuhAAsDARAFGlFgC8VREAISQOAAqsEwAptBQApqMJAFT+EQDwdxIAi+UNAGiOFQBnkg4AadUPAG53DgCCVA8AjT0KALGqCADQjhYAuGELAHa4CgC/ZgUAd1UMAMEzCQB9xhYAoeETANMbDADTkRkAwsATAJfFDQBC0QMA874ZANjlCAAMugcAk/ATAFZtGgBymBUAFdcRADr7EQBZKhMAn7sSAMWLEABcvA8A5vgOALPOCwBV+Q0AUYIHAALPDgC/uwoA+zQKABAVEACBoRUAZ3YTANIRCACIugoAt5ATAObCCgACOw4A2MYRAHnTCgC9vQ8A8CYJAIaBDAD/uBAAdvcHAG5GEQA9Kw8As8kRAKZIEADagBUA/9QPAApLDQA=",
          "dtype": "i4"
         },
         "yaxis": "y"
        }
       ],
       "layout": {
        "barmode": "relative",
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "bairro"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "preco"
         }
        }
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA/UAAAFoCAYAAAAW3NtNAAAAAXNSR0IArs4c6QAAIABJREFUeF7svXlwVdeV//s950pIiEECNAskJDEaMINn8DzgAY+JhziJ80tXOi/v152upDpV3S+u/lW5qrucl1Qlv+7qdP8qne5OPIKNY8c4GI/gEcc2NmAGgxiFhAYkgcQkhHTPfm8ddCWuAV3prH2v7r36nn886O59zvmstfc537PXWtsxxhjwIAESIAESIAESIAESIAESIAESIAESSDkCDkV9ytmMF0wCJEACJEACJEACJEACJEACJEACPgGKejoCCZAACZAACZAACZAACZAACZAACaQoAYr6FDUcL5sESIAESIAESIAESIAESIAESIAEKOrpAyRAAiRAAiRAAiRAAiRAAiRAAiSQogQo6lPUcLxsEiABEiABEiABEiABEiABEiABEqCopw+QAAmQAAmQAAmQAAmQAAmQAAmQQIoSoKhPUcPxskmABEiABEiABEiABEiABEiABEiAop4+QAIkQAIkQAIkQAIkQAIkQAIkQAIpSoCiPkUNx8smARIgARIgARIgARIgARIgARIgAYp6+gAJkAAJkAAJkAAJkAAJkAAJkAAJpCgBivoUNRwvmwRIgARIgARIgARIgARIgARIgAQo6ukDJEACJEACJEACJEACJEACJEACJJCiBCjqU9RwvGwSIAESIAESIAESIAESIAESIAESoKinD5AACZAACZAACZAACZAACZAACZBAihKgqE9Rw/GySYAESIAESIAESIAESIAESIAESICinj5AAiRAAiRAAiRAAiRAAiRAAiRAAilKgKI+RQ3HyyYBEiABEiABEiABEiABEiABEiABinr6AAmQAAmQAAmQAAmQAAmQAAmQAAmkKAGK+hQ1HC+bBEiABEiABEiABEiABEiABEiABCjq6QMkQAIkQAIkQAIkQAIkQAIkQAIkkKIEKOpT1HC8bBIgARIgARIgARIgARIgARIgARKgqKcPkAAJkAAJkAAJkAAJkAAJkAAJkECKEqCoT1HD8bJJgARIgARIgARIgARIgARIgARIgKKePkACJEACJEACJEACJEACJEACJEACKUqAoj5FDcfLJgESIAESIAESIAESIAESIAESIAGKevoACZAACZAACZAACZAACZAACZAACaQoAYr6FDUcL5sESIAESIAESIAESIAESIAESIAEKOrpAyRAAiRAAiRAAiRAAiRAAiRAAiSQogQo6lPUcLxsEiABEiABEiABEiABEiABEiABEqCopw+QAAmQAAmQAAmQAAmQAAmQAAmQQIoSoKhPUcPxskmABEiABEiABEiABEiABEiABEiAop4+QAIkQAIkQAIkQAIkQAIkQAIkQAIpSoCiPkUNx8smARIgARIgARIgARIgARIgARIgAYp6+gAJkAAJkAAJkAAJkAAJkAAJkAAJpCgBivoUNRwvmwRIgARIgARIgARIgARIgARIgAQo6ukDJEACJEACJEACJEACJEACJEACJJCiBCjqU9RwvGwSIAESIAESIAESIAESIAESIAESoKinD5AACZAACZAACZAACZAACZAACZBAihKgqE9Rw/GySYAESIAESIAESIAESIAESIAESICinj5AAiRAAiRAAiRAAiRAAiRAAiRAAilKgKI+RQ3HyyYBEiABEiABEiABEiABEiABEiABinr6AAmQAAmQAAmQAAmQAAmQAAmQAAmkKAGK+hQ1HC+bBEiABEiABEiABEiABEiABEiABCjq6QMkQAIkQAIkQAIkQAIkQAIkQAIkkKIEKOpT1HC8bBIgARIgARIgARIgARIgARIgARKgqKcPkAAJkAAJkAAJkAAJkAAJkAAJkECKEqCoT1HD8bJJgARIgARIgARIgARIgARIgARIgKKePkACJEACJEACJEACJEACJEACJEACKUqAoj5FDcfLJgESIAESIAESIAESIAESIAESIAGKevoACZAACZAACZAACZAACZAACZAACaQoAYr6FDUcL5sESIAESIAESIAESIAESIAESIAEKOrpAyRAAiRAAiRAAiRAAiRAAiRAAiSQogQo6lPUcLxsEiABEiABEiABEiABEiABEiABEqCopw+QAAmQAAmQAAmQAAmQAAmQAAmQQIoSoKhPUcPxskmABEiABEiABEiABEiABEiABEiAop4+QAIkQAIkQAIkQAIkQAIkQAIkQAIpSoCiPkUNx8smARIgARIgARIgARIgARIgARIgAYp6+gAJkAAJkAAJkAAJkAAJkAAJkAAJpCgBivoUNRwvmwRIgARIgARIgARIgARIgARIgAQo6pU+0NDWqeyBzUmABEiABEiABEiABEiABEhg5BIonTR65N68hTunqFdCpKhX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wrP1bfmwV1uB/G0tLPze3w/67VNH1OfLIN0kNl2bkTKFhd/n8z35sM32bK6iPt24o6IxMo1T/rZzz8yp3i0s/tPv/e00F1F/tdq8KbYqn3xEfTbO8rdgf6T673w89SJYs807TH+/bn5XS9RLOf1bEuW/VXh3Ls6oTH1hcIyI85w1U6RturmSWoRSN+T4F+xUHygHka5ct7nt9Puw+a7/tp3gltBC4qhr84WanqK+UGuO5SaBTkogLIy3k342P4sESIAESIAESIAErgmBTIuD16QwfGkkAhT1kbAxEQmQQEcRoKjvKLLMlwRIgARIgARIgASuJEBRX/hWQVFf+HXILyABEiABEiABEiABEiABEiABEuiiBCjqu2jF87NJgARIgARIgARIgARIgARIgAQKnwBFfeHXIb+ABEiABEiABEiABEiABEiABEigixKgqO+iFc/PJgESIAESIAESIAESIAESIAESKHwCFPWFX4f8AhIgARIgARIgARIgARIgARIggS5KgKK+i1Y8P5sESIAESIAESIAESIAESIAESKDwCVDUF34d8gtIgARIgARIgARIgARIgARIgAS6KAGK+i5a8fxsEiABEiABEiABEiABEiABEiCBwidAUV/4dcgvIAESIAESIAESIAESIAESIAES6KIEKOq7aMXzs0mABEiABEiABEiABEiABEiABAqfAEV94dchv4AESIAESIAESIAESIAESIAESKCLEqCo76IVz88mARIgARIgARIgARIgARIgARIofAIU9YVfh/wCEiABEiABEiABEiABEiABEiCBLkqAor6LVjw/mwRIgARIgARIgARIgARIgARIoPAJUNQXfh3yC0iABEiABDoRgeOfNuGrf/IsvvPNeZg1fUon+jJ+CgmQAAmQAAmQQEcQoKjvCKrMkwRIgARIgAQiEjAh6s+dv4BvPv2PKC/rj2e/+7WIJWEyEiABEiABEiCBQiBAUV8ItcQykgAJkAAJdBkCJkR9l4HFDyUBEiABEiABEgBFPY2ABEiABEiABGJEQIn633/i8/jJy++i7kiDV7qn/ujL+IN5s73/r55Rf5N/e+SBGW1eeeWpn3HrRC+Nev6b/+kxvL7wfazduB3TplyPZ779u/j6nz+H4L//4Nlvee8Rb788K79hQ8vw4vefxqABpTGixaKQAAmQAAmQAAlQ1NMGSIAESIAESCBGBJQAlyIpEb1153784bf/Bs8+/TVvn7088/f/8ir+4s++iuJePdtE++Nz7/JEfCZR33zqDP717/4cE8aOSFkcCP57uvD9f5v/Dl59awWFfYxshUUhARIgARIgASFAUU87IAESIAESIIEYEcgUfv/0937slTLTHnkR3Xv2H/b+nknUBw/fy/QuWUR46pkf4rlnvnHFAgAP8IuRsbAoJEACJEACJEBRTxsgARIgARIggXgRyCS0RbSvWrcZEhov3nnlvT915lzbB0hIvT90Phh+n6uoX756I1589b22d6kXyMLCqBEVbdsA4kWOpSEBEiABEiCBrkmAnvquWe/8ahIgARIggZgSyEXUz1+wDM/96BVPdKtr7/yiXz5N9sNT1Me0klksEiABEiABEjBIgKLeIExmRQIkQAIkQAK6BHIJv0/nMTcp6hl+r1uLTE8CJEACJEACV48ARf3VY803kQAJkAAJkEAogXSiXsLhn372x22H3Imor284cUUo/vU1VUbC73lQXmg18QESIAESIAESiA0BivrYVAULQgIkQAIkQALpr6u7rqQ45dR6JbrVdXOyl37yhNH4ZOtuI6Je6iH4Dl5pR+skARIgARIggXgSoKiPZ72wVCRAAiRAAiRAAiRAAiRAAiRAAiQQSoCiPhQRHyABEiABEiABEiABEiABEiABEiCBeBKgqI9nvbBUJEACJEACJEACJEACJEACJEACJBBKgKI+FBEfIAESIAESIAESIAESIAESIAESIIF4EqCoj2e9sFQkQAIkQAIkQAIkQAIkQAIkQAIkEEqAoj4UER8gARIgARIgARIgARIgARIgARIggXgSoKiPZ72wVCRAAiRAAiRAAiRAAiRAAiRAAiQQSoCiPhQRHyABEiABEiABEiABEiABEiABEiCBeBKgqI9nvbBUJEACJEACJEACJEACJEACJEACJBBKgKI+FBEfIAESIAESIAESIAESIAESIAESIIF4EqCoj2e9sFQkQAIkQAIkQAIkQAIkQAIkQAIkEEqAoj4UER8gARIgARIgARIgARIgARIgARIggXgSoKiPZ72wVCRAAiRAAiRAAiRAAiRAAiRAAiQQSoCiPhQRHyABEiABEiABEiABEiABEiABEiCBeBKgqI9nvbBUJEACJEACJEACJEACJEACJEACJBBKgKI+FBEfIAESIAESIAESIAESIAESIAESIIF4EqCoj2e9sFQkQAIkQAIkQAIkQAIkQAIkQAIkEEqAoj4UER8gARIgARIgARIgARIgARIgARIggXgSoKiPZ72wVCRAAiRAAiRAAiRAAiRAAiRAAiQQSoCiPhQRHyABEiABEiABEiABEiABEiABEiCBeBKgqI9nvbBUJEACJEACJEACJEACJEACJEACJBBKgKI+FBEfIAESIAESIAESIAESIAESIAESIIF4EqCoj2e9sFQkQAIkQAIkQAIkQAIkQAIkQAIkEEqAoj4UER8gARIgARIgARIgARIgARIgARIggXgSoKiPZ72wVCRAAiRAAiRAAiRAAiRAAiRAAiQQSoCiPhQRHyABEiABEiABEiABEiABEiABEiCBeBKgqI9nvbBUJEACJEACJEACJEACJEACJEACJBBKgKI+FBEfIAESIAESIAESIAESIAESIAESIIF4EqCoj2e9sFQkQAIkQAIkQAIkQAIkQAIkQAIkEEqAoj4UER8gARIgARIgARIgARIgARIgARIggXgSoKiPZ72wVCRAAiRAAiRAAiRAAiRAAiRAAiQQSoCiPhQRHyABEiABEiABEiABEiABEiABEiCBeBKgqI9nvbBUJEACJEACJEACJEACJEACJEACJBBKgKI+FBEfIAESIAESIAESIAESIAESIAESIIF4EqCoj2e9sFQkQAIkQAIkQAIkQAIkQAIkQAIkEEqAoj4UER8gARIgARIgARIgARIgARIgARIggXgSoKiPZ72wVCRAAiRAAiRAAiRAAiRAAiRAAiQQSoCiPhQRHyABEiABEiABEiABEiABEiABEiCBeBKgqI9nvbBUJEACJEACJEACJEACJEACJEACJBBKgKI+FBEfIAESIAESIAESIAESIAESIAESIIF4Evj/mTy3l2G85ukAAAAASUVORK5CYII="
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# teste_integracao.py\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "\n",
    "df = pd.read_csv(\".//data//raw//sp_properties_sample.csv\")\n",
    "fig = px.bar(df, x='bairro', y='preco')\n",
    "fig.show()  # Verifique se funciona antes do Dash!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b27ce565-4ab2-4c32-a0b4-584f11187e20",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
