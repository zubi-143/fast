# Author = Zubair_Zubi
# Hard__Encrypted__By__Zubi
import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("eJztfXt/2zay9v/vp2DaJnWbjS3qrrZpTppb3aZOVk423ZY5XkqkbMYSpZB0YqfN+ewvARAgZgBeTanKVv1VsQTiMsRggJkB5oG3WC2DyFjYQXhmz/+fe+lO95If+/Ol7YR7X06ty1ar4DOQf/+P/CO0LieT+EuHJzjyF5N8mfOU3/LzmDyPmZ2nzfO0s/N0eJ5Odp4uz9PNztPjeXrZefo8Tz87z4DnGWTnGfI8w6w8EcsRZT332XM/u40Jb2OSnWfK80yz8gQsR6A8b/M6XPJlEf8z45XNknymI7HHFCU5M0zBeN71pmAz72hTMJV3qylYyDvRTBgW8d+0sMubdHlLLm/A5fW6vDqX1+Ly4qdyk4PkESPrTZwy5JkTURl2rHREm6OK+W3y5Uruo6Jh/ipmvOkmGbukYsrlczYggp+TkuLDs1JiEmb7mBTy1+c/fs2nh/KWEu8wem5nEhM3MSpDTzJSMUX6rNN84iWaA04xH6gmH6gmGKjiFV3Q5QuD5ja0WWc8ay+pG80ilP4bfDSYWa9Hf7z5LKnVbGXlowS9MaTHbKL9nLZA/33zBf1+U1sFy3GL08Oqs76kf/ZwrY4koUxupPrMpCuEfDI5Iv1Bs57ydlmbJ1/xNhVOmj0tqfQFfvuaZ+onmbrinW+zGqnQv/kHz8ck9TZ6F/O3OzSd/vtmH78p715K+ZsDXtdQS1gLEjZSCBN9ZiuP+PRmTpRHoh+nyiM+4SUix5cnNp5/E7MVyzyAP4fgpz2CP7+Bmb+FP7+ryDMnlSiJ+ru0jKGkf0/Tbyjp92j6Z0o6VUOcz5X0+zT9CyX9B5p+U0l/QNNvKekP2bt9qTx4RB/sKemPafpXSvoTmv61kv4jTb+tpB/S9H8o6T/R9DtK+s80fV9Jf0rTD5T0X2h6S0k/oummkv6MpreV9Oc0vaOk/5Omd5X0MU3vKenHdFi9oE/p4D23EtGLZ+oJGb8d96E0vlIR/UGbeleX6vMfYs063gNarWddzmby52hPGsv0E1m+/PPFWeDazvPlch4rwVBFJhL9u/ntaLDIfGRmP2pnP+pkP+pmP+plP+qTR3w2ZZ+Vt2obnh9G9nxuLNzpme17H9wwlXJNtsB9e+GGUUjamYFcV9HZ0m8bHy4m3v7qStOnqMCDpe+708hb+o+CYBloC4A3+SFYvg9dfcahnODYkRt5C5c86MoPLqLZUMm9sC9PSG4P1xvCUfAybvvO/VPXj8KxnP5s5Qb2wWh/2DL27vtOsPScbw2aaPzi+d5Bp73f2m+3e92DYW/fePmt4TlfGc+DuBOXB+19s73fbXeMf7lBGPfEQfzT7BMSAQemc9cOdOabiX6DUg/gyzBREyUu46E/4d1HU97wx478RSjmQh+nXXqa9m26Fjx8bV06dN34KDOHiTid55778oMOb7bLvwgLjH75UxrEg92P3Q+m50HlQz+QuNoI1gYxpZAcwgCXs4pa33Kl55VQ+4/3LDQjHYUWmkzS2fbPzGftxUHms97iTuYzc2FZYWokJJ8gXTGeLm3H80+NWDZHsQo6GqmfyejenhXJFUTwpxe5QURWOnUSuoqnIWVKdZa+KzjAP+EVLQ4WmzBylheRUuv7IG5RSZ3NL8IzpS0+p4Os4dx1V9o1ASRM92CXtlpKAp8i03c7VdageIVcxKvLTVxOOzl/lhDRT/522d8J+xvwEQm6KbKD03jxUjpfU7/SnvwbT/5w5Rcz/JMf1en/TdoPUHygJICuIpJgziBBXDP6Ix3AN9LUj8bP7vzCpss5GDwRrnsZr7c+zgEGhnvpRcX8Lctw0FPnlMgOLtbFdSWdR5hG5w28MuMCQMIhs461nPpo4UX5I/9ySa05MUk+fC0ed/gDuIr/yevSr/1dwAaRWZ4ixRLNrGX6IOlKYhizKTvpNXMwEKS+5Y6DV5FCnlw/HWGAEUeKLC7Ozier6XMwfXHKQfff8HAWRdfbwyxSBkJg+85yoRBBkj0/UqbAeawnWliI3cg+17YEaLlUUt4rKY6S4tUe74Aae2qfD2EhH9djwWmN/aXTGXnULjP8QR/C4f9/gEILD//L+3zQJCrniD+Go/UNr0I7voBwqBLQRgXNvpAdIRdCUsBQh3oEmXVT2RBK8VvmmnwlGhfiNBB59IT1QW5t5TmKNWhvoCcZT/NgMByN8UoSWmjg37gZKmk3w289vD6MU5d4xui8QZPgSPKVeUGRMs933EtVTt3V3J5qVJUoQKsLMe4mOAGsv4oIj7mLTk5wQYJhIZrBe72pJbzj1GnIPvdxARfXYikiazGz3GRLeuJHp15f7TrWRr9BZ0JBBr8uqU8RDEAuI4OHr2maEPEclUS7GFmJIqWW6UhZW3JW1eBUpgiLWQFsLCArALz1kWaYntrtl62vrUt71LmnDNnKA27M5gv5uYsTgHAp+pky4j4oKW7tBQSI3xt7bvtPcakhroq1biY7Cib7TQdkmIxqiTiuM37//d0K/5FeTksaqYl1/yI6WwZGqpZ+Y6RG1G8vf7h/ODbiP4eZFTzxorOLSUYFZ1G0Cr85ODilmfany8UB8YndMbudzApfndlReH+1yqjy9qjd6XZMczTotkewkiodYih6UBmzAjAcSviPeIhBCZSEXBVWWu2TH1UXE9lRYundNEsv/dpPvw7Sr8P86qR5P9umAZokWeqg2HpfwFGN9CJhpF+6MQWjuOioE+7r8kgmUXtBh7+wiZ4uTz3feLE8d33jcbxeTZbL8/AfxZW05UoeLt/75MxHUk88rspU0Smo4k5xFV31VV7FUpC+CV4WtUainPzReJTYdsqCqxiNUC+5CiN3oai38+XpkiSC+Xblzb2zk4UdXpw3Z0WCSZHWPUGlTL0RyVdlakpaEfhV9JfmLuMozhHqePwqrpQWFylFnFV9VYigtLvzJX9AmcbEUa5KkBnL1KSvVNcF1YX3lAw92N4hp1vrxojbGHWVKuCGVGgrGQawjXPehnZa8QOl/BA2wEtIeSLUa5dDhzfS1TbyHFXg4yZsVe2f4EbsGW+kp21kX6liipuZDlCeADfiCMVO65j1LekgUtEYgaoYmE+Ows/kn3weaS2O5+40Mp6tyHZTSJPJEptOXYZqjnylq2mw+F3rzXptPPbmc+PBMgjihuZXxg1FvzKlAck+LAlkaquZ2kqmjpqpo2Tqqpm6SibV2cYmONATyEMc2O9PPH91EY1vw1zYMCMrxwdlsrUXE29+Qh+ibVb2ZO7558r8OSdryRhvTGq9vmBSXZSa0nWmFXi3Jcht4PIJGVP0l03J3KIaXvtX25L8i5gAvJbk7gROQelmFTcxJTqWZodQLBdXZ4BhBXt/uAo4m5DCYgYStp9yiEf4iKL0cKXwp8in81T3aeJP8RFhsHOkjPBAG5i5EkVV1+lRVpdPdZW98r/mvI/4hMuP3U24yEkntvy0YZc3POOvrz1/F1nwRBqYrmmuX+FcDAZmTQW6CxXoA10eSV3sLe7J2iJTVyUrSpriQyDTwkwL7NXZ/izRUKm5tnDv2dOpG4ZsmrobwgmQTkb70WWkeHnCTgG1bf5yU/JyEuESmUxvPoyM98uAaMwk/3BItvRC6CZ2Tu8sV/Hb8jd5//49fA+TrB5Ds2/Gpmd/2C7U4NH+TJrMevV9sPRPjRunHfofOT5AXBsmIEpRzMdgGR1/DX6hZQa5CfhRE8Vnd+pGykz/JlyqDnd68F3dRnQv1fKkJxW/i+rBny9DF62Hk2V0cr5cMH8/eIGf3St6tKXYXzMG9pl2iwDQQcaluuewjNSNAlt50w+u49RbE5ETB8wJLax5JdOP3prhS2Qy3Zj8Lz+hMpPK+qAGXt9EUzv9dU2Xxk+43/Ekva6VkVeitqc9cqlfObVHGTK17ryTDY1M3linNox0ntvf33+xXM6JayH+GlqWnFGZ25zAe+funy6Xp3OXzm0zb+4eOAfms2533vvpw52TN93F2/ML79+TX98+efnrufPPt6Pe7JenB+889/29i3B1l1YROuceHgDKy1ebxPZQ0cqini+IpSRzBDONlI0V/UaATjh96UkTAnVX/iUGOJMSuN+WSolIl21rVdSEhz9XoDL0y5pSAvek6wgFODuCJGJ/n7vKYk2Ge96Ma8nHoN/5qf/wp8MPS/fJYjF60mmdhkf/7jw+vN/66cPV21rykS8AubKDx+Jm5OMbmMk2cYEsn1llyZig32C8KI42EXtgXVZabUiEjs3LiLUGLzp5m8OqNZGYhSR/V8iN0DxEfEdqZLgjKz1TSj8V10vJk9/lmfmhkmQmEJF0mSubyKHEVyk5tGEdWa0n5hj5IllO4tCgYjABs1RkU4KVJCM0gxNXXKdO9Eyx9+nwXUD4Aq987pDoJg4VYX+mvHI0BmEiiezFtCZmauclFqZEEi17YiXSmz5II8e4canYkLR96QySKMqHDPvynTiAoctCH3wnPdH6eqXnSmcLC19EMwkL/pyPOOKEJV3XvtpPOs0UrmOxfy3FxbCDT235SZ//+MhHmmeloZkmH50s6KgvIotEHFFftCV6pi8iiUTcUF+ECYkAIZg0Y0l0rLDgmz6LtWGRNX35lBijoM9ia1gkTZ8FziRhMn3yLr1kGJt8hU3CMeV4MjHmhVNfBEaKFO3KDbLKoi1YJzw+PVCjONr1J8/DInX6iuB/DQZBxFnwhr+/GA0sdEc0JQfDkeJDXtzmxSc8v6hQMw9ESTE8f/9DyppM3onfiQs3Y+qfiRcrseoJzbgLRQFXJxsskkjrijrA5FqJO0i8EBPuVgYhmlPaSuwiSX31lsuXxVadpAE6PllYpBRLOrDQelNmDhMt/JpGBonxoQg7WwKddmbP6DVSKQDT0Q7nPPJcm7bZa7zNm7oGtb47qNUqtl+WA0zxNgR1FGLgVpBOPbyyA9/zT9ODEP3Fw6VxtIyMl6Fr/Ht5ERjP3SBc+nZsRU6nyws/Ctvl6yKV2MaR+54XjlVu5nyDbrz8Wl64weLi0jDuz+fGOxbEY7xakt1B7ucb9kLtcf6B1Av2NO0bagY8ffbk8Mh4dfjiR+Px/QePfnj27Geari+sHkCKwq/1bf5++7WRtnX48ODRwvbm6fNvpKfl6nhuh+H7ZeBk1GGhA4PcYlkAX2XIwy+Tj3TG5cWZG7iGFxr+0vD8yA18NzKmInhM2cHyA+WYi+I/c8lLK56xVfwmpCvhRr39zr3juO+8qRs+kR/YK+/k3L26Oxy27WF31Or0TcceDQet9mQ2Gtittuk4U7PrTAPXcf3Is+fhSXS1cu+ukg6jRNwN/yNXOlsGCzu6+9Pxs6NT13cDO3JPFvb0zPPdE8+5a4rE0A3JWDuZxh3oueFdc76c2nP3ruufvDxeuNHZ0rlrX0Rn+1RYeZN3w2+BuLrRReCfhOH8JHDDWKDid7zbenfX3G/127Ph1B3NBt2JGX/tTs12Zzolx5AGdtfutCOwC1bUB0INR52nuEw5odLWA/vgXlSYR7pM2YNk3TkGju8IW6iajhYrkZIH9bs6skj/K3Qw5qDpMGWPkp8xcNzDdIM31nGPDF/wcjErlVn6neI5Xjg9JS30TpFUctGNmQc3GkgwY+gG8fy3vzpbKW+zsgN7ESq7JdKamHSItOkSgoUknQ/6C7Y/cnxBM88u5vvJFkmc0W4ns+KAbZmk6fv71908+UXXE9rNo4NZ4Lm+E95LxHC1DKNbF54T3j197y0uQrtzC2wvoW3w6Zk7PV8t41EBXUXynEgXP75sxVNjvOg8SIth2QkWxp1gZohlWxPpioN3fHV+ZysFaY1uBO3dkgsUuX1+wIyH2/SufzF+hLOACePwGdtKyXM9KdtJYF2YBGjjRkQ8K7PQy/FTvnFjYhmElL8ILtTiJ/GAiJbBlfISXnhyFi3owgPXGJccTzkhs5XSAk+ECtnFZOFFSvIpmRHmSrNndng29yaKhPvue6WKixWNnoY9deZeOt5pLORj4M0dfw9+3QO/AHjUGJxMV/bZxsAxpq7LsQCNH8IsQGTcy6nLjvaM8dCu43CEh7Ef544qulbAbl29V9NitoyhC1d5y7jf7bGFAwnAEdsx2J0a38L1Aa5f+N55rJDWc5h+CzPZNigQ4SoseTeBGyEzS96q45t82XsO8r8RyJX+xWdsBrBNdJ48LcdtzCl4LvlyxTYjboHXTEMmjsGrBTArXZ3J7yQwykwaR7uanEjtvqYpEyztjIoX4R7jqaZ0+iJt3ROduxqfy889NsR7lyVccT+JGA26LZ3UjfEmLQwdOfTLKz8BeJEOrnHTn08zwO6XTgmKQzfCj6u1h6Hl2+PNC4r7PEU4ZAY8RewyDXlK0lTEfyebSz7/LQ4WTXjKgPcV91eleShnkEsx4F8Lg9/V+lxeXzetT8x6iouy8ZbMllxjp+GWelbWO/XX2BJ8p0GdlhQvJh/K9MexcpbmKPPcEVgGQmyrSIb6jdfJiSjPf2fPYxW0SDWMLLQ6EjXY7JjDXmtgtrokOAc+P6TOmN8uJl5sEM7ipFH8eESOKw0V2+j+0ZPxv5UWRp1B/N+o1+l0hp1+T/N8OOp1W8N+j/zbUyh4Erh2pKNgaCpr7NNn/3oUQt2oniav7KnfQifGBNJXYTMhVp0P4lRynCg8iNsNQ/vUvavwLTa5bOr+CO9Rn4ISqVmgcRNAozFY1Is0eKj5rcAv4MJQSVE0KKga+baSdr5UFWHyxrBdZYAR/rSVgnFlbSUrqa1dTzd6CDO5UDf6AldhQT2CASJCLYgJPmkHxlSX/stqvaH5R7fo9/J+40XfsS1p0a+wwwv0gxJ71Np4TUk/4GKbbk5z/eBE6mahH9Ac+nO2GQTrs2YeFtFHS/Bcv17d5e8OzygLTaPcAedkwyXiJUz2W0HwBAHwUIEhfNCDQQzlx13WzR/kbka7yDPOA9HTFbpXbKhX7OcpyxqwjFro0kx2XLc8VEoFI+H56bR/TAXtVGiA9LWLTlNXG6xMW2DnJ5LgGa6MJAGUQpMROhhLn/H0LkzX1mJywTclnVGoKuZA8qeyJ21QaUbxTmbxbpnivczi/TLFB5nFh2WKjzKL27A4B1iDmaZFvS65evO0ReApKL9rp6qPYO394wY/Rn/IlEbjRqHaCONL83Wqe8j5iVZr31644wBTqIUW6lMFl//ix9QTVVfr5DTxix4tpa2kOpuX3+rySGfq+wvonlZO/PcWxtH9Xx7xn62FEf9393v+m8QtNNHGy+NHY+PwodQMbMPKAB2Lm0EdQfUN3kKYChP7GA8Ce3oet2Q8prrzwfOLydyb4jpkKsPPsypYLownwfJiZRwktRnPlxR7ElbWQQS5OfW9WEb23Hi8nM+X791AqaqLqrL1Vb0MCc6aTWyfgAxYXE0PVgNNBeMl9bEax9PAW1FvPTq+WxQTTWoEOpvxQ0zXnoWc1ZV88uM/wS9oGgDpbsgHDNz9Jby0b/Fj7OZFLw82ChT1/z3Zydem2qpVQcLD93AqtGrGYGsYem11U5wNp7h6hsh/cCa5V8Kn2qfISas1RwKQxl2nvAT/y7yaXHlxNSV1tQ2kXz6sETlrdY5i9d/Uy5r/N0jLXDc+/ks5v+r8XG90/GyqVNcF1TUQHe+owe8NR8dbl5OhUsUaAuTZMg3qWEuMfKRUsYYY+bHSiIsbcUdKnhluhq7XeihU/f0DabisqQzw7Kra+qyy/SXzSYT/m0VCAHVgMLEeQVUi1W9A+D/TGAvj/1u6qjKjJdOvBoICuAGPn4wBJMwYxLeOQZtjuMKBKWkMF3bQC1LPsU9P2bVs9eDZkjHCp1IsCbxh6y6W71yDndQoNA5q9yTGVFA3Z3Hc1lDBhgP5p0SBO4nche1nPJt75+xUz1R9NqNao7rRGiuB7MwQOsvkBhM7uPCK9DAlfiYf5GD8Dj9u5SboNAfcUbflRvCxPyZ21voBDtJfsn6g2dW8ZkhavCqA3BV9hLTmEshV0vLHNqtkpwXcmoNOi4zig8ziw+LiUUZhv0zLk8yWgSsj4IVBFhe2oOuyzIUVzPXQIGgqQrW22QtEOjUND30CiR16dq7Ji1eutPwPtn86tx03PMs3cwN98ZfH94ts2ra+5HP73Asj22/SIMW4h1XiasnJaZygrHMaHC86uzcUNxg3CSxhsvVjSgWqQHg1a6CAflRuepjIJVQTRdIQmIwK72ax8UIfpfokvzNJtl0y7QpV50e2yxMlA7Jd/snJz7QrVPQwZLt4SgZku4S8jUyboqtUodouE5RHsV1GPH4qw6YIUAWq4eIoZCiGy0ScOtHbFM+VKlTDZYbyqIYLtDpKIIgphsvMVPIohkt6XYn2JEUWhph2NEIjAgjbkWoKcE++KFSEJtacyrtp42HMTk7DBLAc5FkO6t6/oqArczpY1fFZaKp3e/GSmqGST+hqiY6rskcXoZ2h46/ISqceWjAhIfjuIN97V3sRAe/4T7mtrPMC4jDh+pXtyqp17nkBGwyuTZ8XsC2xkQ3OCyTLSN3zAvmIEerevi6rHH0OJq0ae7/JTrpjqdHt+th1aR9aTPLZ5TPcNPKkCdTP6+w9Vt/ZK3Q4KFt/dSyDohm8g5B7mR5N95iSvap5rE6HveJq2hnVsJ2z+HtcGa0rA5FSrquTRZI3d5WtsWLFXujxGJ+89sYS3DXBJ9CKNoGKdnkAY5k5QBaPxqwB6DcQV53SAjr8q3bt/RatCVEX/Rej/+SDQw4tybzY9P4GPb/Rudb+BjcCxDoCcIIy5+dkASgxp2ZNmuphYp/Tob1s43oHvS6JHtEG57m4n2ZELuIz4el1oQsR8sQmkugW7shRUATessO0/KLndqYhQIaOOHAkeAM1/biE2+EdXo83GFWEn1Iy87PI41jdmxDn366+532lnAtPIUJk91Z6XCmXzcLWw2zu5bBZtCx2qEQKdxiOmGPtlX+YvB/GAuXahKzrmAluPugTLThOZInJI+9gnOirWfKF9bwE3TDVkTESZJhZ04GkHJVliDiCtS65I8qEWUbuhO2typ2YQPLkbkqndYLMNFMEy4SmfpiYxybIA215MjFS7bme8F39xnNmiaBjlRdBF7cmkFQu+brDxFTAqDipsgiMABXYh3IhuRYqyuJBxItrvDyIE0S22q8IVglFxm9bOsjdoYKGxbB25Pe+oa0eVptIe1qxPVMq/gxXXFl+RaO/Yu/M53hcTalCkmb4Ag8qilxCBpWp9zHxPmdAQnk7u7c457nkmBxbRwdQLH9nuwtfJgOQanMM9oeh/JzygZ5g6VwmSovPhsseH4AMU0nA/Yh9jycRH1FvLIzzozlzbE55DioSANJH5jud9jqvGHJOTHcCyKNe5f2R92HERcdRhupHK/EYBrxx4bjjRUEvcu1W4AA5fAltZ7DBUF8D8oAj1bCDsai0ZvArHCxY59MBn2mQo3lNO6lJdiy6zlV7fKCz2eMDlTyAVgN7YOAkniH/l/aADEOd9d1IX+LB+P6Dn43Do4fPjh4dH96vWBHE3ykXoQUOFY8vQCcBX0We09RrV+m9LjlxG/6Prvf+qo57oCMYeAgkgIyZbOinOchWIPU8JH2bhaaezn+FfCLGNLBBEb669sL6MmSnGYwje+FmkDpGU3Qr/K6ScJLd0RVzxhwYSac4S5cgEkWGe+mFETsiD81sPyXuj7Sy74hH5fv00UeMfFRIDDiyTtsFM0CGRORsB1SYADgD9N8rjOP8igr5U2Yc0wFB/F5pPxpgVEBXZNENWYgLpGIjkqCpbhg5Q6C9+F3qHDIEJNzf1/Bigjpt5+3JZK1EGRfZ5KxEhYEIZdjCDuDHEpUxrbQbaOM4Wq5IB/nGgxfjp7d/I/MP2MzZj8e2mrivTdzHNAU1qWLu2DCyg4hED6gBKmBAynA/0m0XRc30KK7dfS9YzW3fNX5ZOq5xOCOoeWek0cOQotPFX8PL4sXtU/zO7m88ofc3bgE56/iuuZcVbohY6ITiMVRryFlkodoIw054Ra7+Rf5V96MkIGIpRTgXuzxFOc4A0BW4cZF6R8SpEI1VAC2E7GdFkbxvwOU6rTQjBEzGG42iRuKEEdFjXbEZza10fkGUMNGlOOBDy4+ETcbUIOHVxjDC8IigALfQ+qEiznUBiyx8UhgOWRQUHjPs9TFHWk8KOHYonKSRpWD+atgITh0iL504dZjlJ03fTJznUUw+FWZFuEhTSFc6VsGWZ6D0AT+hOOJ+BClCFvgXErJQ5KywdYUbGvuY25xcEQMgzstzgTJV1gCygKs5H30aeEPFyVI8omUqTO3etOrzyLx92X9hRcKxDBzVIsRcRtmlkAmyC9iRW8jhS4qsjPgiHKv1+CLGLsc3Tvni5JO1Fr4IlOVMvnBvZhFfkj2ZYTWZN8WZ3dSBWl3iozR1c/JuXdoUIgueckhdYdcQ+ihN3S6Rj+T0DQk8ZemwtMyT9+isQeDr8WQD4l6eJ00KO/UYD6oIu8FJ+yg2q6tLup+mblLSZ8NkVDUt6VJQxHZJui+nb0rSGSh+v7Ss/1/8b3cNsl6PKxuQ9fJcaU7Wv6EsucHfUgCN1NDLJ2n65qSX0Nlbg+jKm3ZbJrygpzcovkPe12XV84nNCzSuntdjzkbU8/LMaXLFpic7umxHH+zy1hDkaZq+OUFeWWxtaF6QpdjCbRPkqfxkQ4L8o5UsqyWleNZPONO8FNfjzEakuDxnGjWyyZt02NmZjyIOtroMB2nqRk1m0muDNQhxkKZulwgHcvrGVmLavZ3SMkzeergGAa7HlQ2Ib3muNGo0k5ba7FzbR057zSXYTdM3KcDuMBkqza/CUvj+dokw6OwNCjE9eWeWFmKfecYbX4Pr8WUja3B5vjQnxj/xKhn1Nznp5ba1OLxTHZGfpembE/m25a9F2mdp+rZJ+0x+sjnjWch2WeN5SFnTvMDXY81GBL48a5pct1k5sjMvTjto9t8dnvEY3lh1FPI3F5/gj4/w6KklwlFv/mipx5U6i5u/aJLbi5vH0mmvMQyFDfk78k/BuUkQAKmA54ITqjMvCKMTgkca4Xcz2wTrZmTqGp7cUS50Y/cdHKQ31MF2253BoDcatUa9kdnv9W62e+3e4EFrZnZbtj1xndmk37On7YE96Ixcx7Tb7X5nYt5KLjd8Ey79W6FzfpLcl3m3fSu5CpEPa/65JV9qeCu9xBDAa5Kq7nrL8Fb23Yi3Qu/0bmfW6/Vmo1FMnDmbOgPbbk273VlvOOu12+6sP/5fwCZ4HlB3GKu9iA2/DjuMpR7Eai+OXz548Oj4+PHLp2FXN6oKq6InGKVzcuRE5vdSA+q51nrtEBTbvHZqVssvjpOrBtXCIHICm3RAonVpnDhgMYqt9f/gzX000k42QHrcd7bBXiS0EPAzyMhevkRG8To0YwtlDC10BgtfKIgwKlxyv9zJIjxFaGu6gdbJHWidxYNHPz9/dnj0opBP+opYV2Wxv1PMfn21+aOqdrX5oyqu1sjkIO+nzJEijrFJ02a3vvDm9Gqb3m/Sw21RpEZ4ete+sv1TcV6OfwjuSWirNwDa/huPZQfJ50s/Ws7REJzbyWqxZ13CsPExXFfieUYBAEB4kMf4MZiXlOXIZzCKAComjIJZ5C3c8ReoLhO1HeDnSlugXxfnjhcoHfjsmN3wmAdmDbEKSkNbKxRQqHGFJxfBPLmUcYCSycWkylCcL20HISsotyaCjlieh+rwWMVVq0iVU5fdHKpgISmV2sGpQtmH+PVIIjglbfvjm7gmUGqyDE0Yp6PUcb7UvJSq28TU62pXLwKKEzu6xK4usadL7OsSB7rEYS2ICaWmWC/ykxBMseCEZxZefthvfikQVZRlIE1+c1/yizbR5hkTATMtcVEhxx4y+Q2O/K/u0sFI+jfJ+RX9wUGGWvBv9cLtHUVlKBJ3Qe0o2lF0DYq2aGQnlLB5yrNQeFUIQmEzFMiioJzHnu+FZ65j7O/vh8cNVMjim1I979nPab4DSWd/LrkIvgFWEbL5tcVD59qkliGts5iRWLNj+x2IrZTqAFYbMYKyCPsurZPEv6VPvv+ovPLqKjpb+m3jw8XE219d7QHzT4EUHFW69QSCzK5B/UPhxtalDeET8cUnEFNq/BY9bpkoASFgoXsegYZPbnmcez4DNAfFYmXbWyH4LQCIWKiFF1kIuBeKob2gdqSoeQt7RToTg1PCq6n3cEOKRhW59nnRPdqgy0OFEs+JlLTV8lzRX8PV2MBVw2h9iuumqvoxyxSORV7knSvELeMemIxwIyDLqjbYGWj/o1xvyEGh0Id0STZKPFlcgFqqRTdLfqF7ZtKrvYdVa1Ku8sbqrqmpyZf+zbqhJqumfBo5Hbm0mlOJVowGF2TSK+4H10F7WuK6dHHLOP8L7zNXTQe5Dor2QuiduBK9LVQj/fuV5hUpoTuUUR3BO5RR3k30R2Moo2B+1+hKKLx+Bza6Axu9LHWlHJjGGNwoA6RuDnDUhPlGXTnbDnNUZKN9ssMcbe0wR9eAOVqbN4KkGW6lFOKoGOZdzkpx4IP8yGXy9RBH2zw3BNu06iKOYr1HOkKi9vz6EEf7gox6iKN6hggerEvqiEbx1yOOKnecaBBHRyBP0BTi6LUFkKPCwt4txBtV8BK3Gm80MRuxnDnaRqqjjnKN7lpiLNpVgEcTj3Mu9qiBh1dp7FGrWBNg0ZQRl6eID3nBTfiS8nd6WC9BZWVRIOw4OTuHWg199BbvlqbQRznAnDIAOPzoXkL4V8nfRM/NhR+9jeusDz/Km/1H8vdOBhuK4Uf3+TdN6TLwowdWyQlFK7eaSU5rWEsGLlD4M+BH+7XgR4vMNxVS7hqgo9DrWQo2E5hmWszBfj3MwR/uHz15ev/ho+MfK9b0l6GOFqJ2YvoF29IMxhaidpYhe3tRO/vZqJ19do8i8Cf8cYMic3p+5Aa+G8Wy1CRCZ9Gbl+5qCh2Z0d/QaXZQrbNpxbh7rwGJWbS3W6b5XFTMIizLMl1ahGVZ5I8r0wbFsnwwX/oEvrEZOEvI2qAmYRKc5Q7LcodluUYsSyBG4IxGPL6dTqpvqLsbDWJWZuuOqhqoEjHADViy6Zxib3LPBHYU4M0p0RxGpqSdkbkHJeFSulZ6B7qwU4XvEwf8yMiUAf+q9VYI00+4Z4Tn4k3KXFiww7Nh3wAL4FPMNSWAr5u0bEIrvVQAn+TLKQzgE29mil6qF8D3wrrcBC4lD2PchgA+4DMrF8CnNeqFcSfiyLKjxFaVcCmdjeFSluTLtuJSZvJFeCkK+JJggObgUupkXotLWVniozR1c/Ier3cqLmUTIh+lqdsl8JGcviFxJ76z8qCUxEW3AVDK7ZH18ixpUtJt8iUHlFIr6SKkWMKlrCzpVXApG5R0V8WlbELSEf7h9kh6DVTKa0t6vFiTzi2PSkmI3AAq5fYIew1UymsL+78oSwz+lgKVsoZWXgWVsjHZJStCr3HBVWAPt0d0a2FSNiC8dE2ogklpbwyTcnskuBYmZQMLtsn6WoDLiq2/GmJcBZOyMTEmkQz9NYgxwj3cJjGugUh5bTEm9FZBpHQ3hki5TTJcA5GyARl2CLmdKkr3Z5w0CcCyssAHaeomNW66Ogwal/ggTd0ueQ/k9I0t2lRWy8NXkmIbgK/cHlkvz5UmJZ0dCU/J/5zTXs5zLtAuayzuVdAuG5T2WdfCaJfNrO8IU3F75L0W1mUTNjb9UlriP2wG63J7JL4W1uW1ZR5hXRYKvOw2l7Auawh8FazLxgT+e4R12YysIzjFbZL1GkiXDch6ZaTLaXczSJfbJO41kC4bWOJZuQpIl19IbWUhXWovHa6OdLlGeMsxi49Mn4/ZaSHQ2g7T8lPDtMyFxVNPfdZr5y/DtERDmuKjsKDQ/05cyzGGgigBaNnPHWX98oCW+oryx1i/mPf6avOHVO1q84dU/1qAloQ5EH0mTgDnlsnkDebYwbAf/4+QhdkAdtzwLMJrSZyZVAoG/Z6FTkc3DSg5TnYQQIIJEwL03FRqaOMEmGMd2EBxI12cgOGLbLzm2RDxKAcEcqwDyMEDQEHMgQJOcmDm2FOc4ICEm/gxDK2/wI9xoP0EUzAxcQJm1gSzc4I7doI7doI7doKhpCag8+oG7UNAnuQmJpFND9+4RxOD5BFAcrR28I1/A4q2Dwhw+yjaPq7tKMopnFBSF74xMwhFUo4qwTeWqbAUfGP/2vCNGVkqkFqGtH45+MbUPCHavpNB2ndprQ0DOE5xwicG4Ah1lbfocQurMnkAjuPk9lWQALWxbQZtJNQqqmJFxEZSB9Quc9AaxwkMnUhQ7BPPmYyTK6zBmINcMfBjrG5Osbo5xermVFE3seI9BfpnXe0SSkvSnW2pjBaZUV4BdsiMO2RGzSvukBl3yIzWZpEZLXHQn3+4ivH7jdeSyrKDZNxBMl6WgGQEg44BMl6EDaIxtmG+CaFO9MQOjVFko/20Q2Ns7dAY14DGOEsy80VA4Y0ugzyKTe0opi3koTG2+auJswJOOhGuFY1RHKARKfxQQj00xhQGMe2TAaaA9/z60BiHgox6aIx6hoxKMeQaUkeUib8ejdG2LgvRGCcgT9AUGuP1BXCq691CNEZHKsXp32o0Rh1cooIEmzC7Khqjoam7mgyLRhUoxht4bGEcxs/wwCqNw/h5SrZW5hluYsRfJuLThGAifD35Oz1HdjMZhbdYnzDFg6p31VAYv+I90hQK49cqwQCE8XZCOEBBtPJBGPdxnfVBGHmzHAJRiGFlEEbxTVO6DAhj2yo5j3TUCrRqRVeXT7JlgS6cAcLYqwXC2NJVlQliln69JhxjDWsXmGwG+i/thFqIjC+P71es4i+DYqyDZFmE3lgG5yxFb3y8LeiNZcjeXvTG3uL3tDKI3thbvK4omHpgR2MjyI6l2UA8PCn5Rg6y4/WhFbca2DGDt79rG3idM+kWQkSW4c11ISLLtPGXQESWIYw5II93EJE7iMhGISIDyMt8gEjqbhJThLrNsoOIZLn4R4KIJFpUXzWfhUsWx8psACRSeCoA6iPvQ1MwcqCljztrMe5dlEWsGszW4RXnBbP5PBMKZSO7H6ZuL07yxPKOk4LZhPdHtpPkjuum6RF3agi7CXs825zYnGC2dh5RwO2pxEt15SfAMydGR24omyJnVmJQ871WE/NWDWUjHdYTnk7gOeUeQRjKNrWgT1I4EnMZk8a7QcakIW71GJMTypY7WtbCGBHIlskYkaOQMbSynvDlSSiONSQ4StM3Jb9xdkJfu3ERjtLUbRLgSE7fkPgSf0a3guy2ONpes7JbjyNrl9zyHGlSbun8CNBkREz5SHJqA7TGGhItQdZtTqLpqbxO4xKNcAG3RaIBKuDGFmTaWZ3SQv3USqaARiW6HkfWLtHlOdKkRA/pQcgMiTY4FQDEsZaSLSHYbUykyYPeGrRsBBS4LSKNYAI3JtRTgZZecqUetRLGNK1l12PMBrTs8oxpTrYf8io1gn2DkwA2E2sJtgRrtynBPrISWMeG5RqBB26PXAPowM1Zz0KKS8o13WHtr0Gu6zFmA3JdnjGNWs+0XAUYGHAg9ZOFgRF+Tv7x5st37tXyItyhv+zQX7YN/QWcvqbhlRfhDvoFbOllD7FeeegXfUX5A6xXzHh9tfnjqXa1+eOpdy3oFzJrgo1xs93p9ihWSz6m1rgQM2aPL+9pjh28C2/kr0Zzwf3y34jl0gwwCzGGulIB18a1xJ8mgVm2D1BjCylydxR9QhR1LUkeqkN8lDngUwnio/yRrFRr0+Jo9K4H8RGv3dNrk1qGtB6D+AgLID4SHZSodE4GXd+lVTaN74FXnE8M3wMuV2/RY6g2j60dvsc68T3GSdStSCCTExhOb5bnJA0wbbn6pBA+0NRBg2s6UpkdwkdmTX8LhA/uglSX7R28xw7eYwfvoWtzB+9hfvLwHohQBvCxss+9sDmID7hDwrSb1Euwg/jg2WjX7SA+dhAf1g7iYwfxYe0gPrDU7SA+1N7dQXz8DSA+rGIdgMGARPx9xDEYScXLxYj4IhmIdK8KYH1UQ/nY453SFMrHVxms5ygfXyeEA7QPKx/l4w6usz7KB292P/l7kMGGYpQPLvZ1UT5M67JIz2LjsJ014NH01tHlk0xa4MzLQPkw/8tRPh7KebQQH2Y9iI/n938+PH5x/6hiPf9VOB/4ldX9HFPC+ZhtC85HGbK3F+fDzMb5MBevEYxBIS1HS+NQwfnYCMxHaS6Uh/mo+O5aoI1txvkoQuco06VF6BydBtqg6Bwv3HPb3xg2Rxmydtgca//+t8TmQM57qwCdI9bbxOKr7pHssDlYLv6RsDlcy1etXuFJVWJ31o/MATyN/GrckpfQd5OW69xJLXmGRChlcSCS6KW8QKTsO6lfWIl10fCt1N00XfgIhDtTOMQqhCKprKl79THwwG3oVuoVu1BevF/+hdSOCEhs/ErqenzZyJXU5fnS5JXU9LDssJrMy/fQc7dddYmP0tTNyXu83tHTHY2LfJSmbpfAR3L6hsSdOPKGpQWeOEA6a5D2eizZgKyXZ0mTkk4jMQYVJV0HCFJZ0iVkhE1KussBZZqVdAQ/sT2SDgAoNiTp8WJNOrdfWtgJkd01CHs9rmxA2MtzpTlh/xdlicHfUiB/1NDKJeSDzckuWRF6a9DKEb7E9oguQpjYmPDSNaFXQTWnZ8J7bNexSb28Hmc2opeX50yTq7XJOvoz/qpiL7GGDEsoB5uTYRLw0F+DDCMsiW2SYYAmsSEZJvR2Kwiw20/40rxtXY8zG5Hh8pxpUoYdipaWvsDnnHq9uv0Fpys5F1BL2oM0dZO6Nl0XBo2Le5CmbpewB3L6xpZrKqid0tJOig3XIOr1uLIBQS/PlSbFnOygyBB8BWJuIZ85fdWaK7ubpm9S2mfdZGQ1vbi7afp2yTvo6k1a1/RLaYn/wPzsjS/t9fiykaW9PF+ak/mfeJUlBV52mCdSUFPgZ2n65gT+e8tfg6zP0vRtk/WZ/GRjsp7i9ZXU5afdmDH8orzGZL0eXzYi6+X50uT6zspVgOsDke+fLFzfuBBhKtzh9u1w+7YNtw+ccqSYKTSwdIfcl3ZZ3iAzyyP36SvKH2JmMev11eaPqNrV5o8o81rIfeNCAD5xuox/6FCNbL8EGzsl2ThOgoQBFThcewrIuvYg6ojW97hakja2gxjkjXRxwl+NOYhmm/F/J+rgmMecywkY62oCOq8ZoEJ2oYEocWbhCf+yUZhCDuq2BfByLUbpjqJiirYQynHrKNo+ru0oyimcUFIXXLJMFEwlcMnyEUWpaaFFcDSvBy4Zq5fFQD81wSUBaSYDlzwuAJcUhhKxO5wMyr5LK2gYXtLBK/0nBi8JqX2LHreUt9vBS0oJ64aXJEYOTnAg0Z8QsiQUleTlu1KZHbJkZk1/C2TJZEg0By6JxxMCzINGeUjJE8NWuKg3hC5pMYwX+h0BTFIZWQPApIJ4lI3Row1BlAICudu9Qq8JP9K1ENEilqqFU0r46HN6JrwGsZ2UvIqZHgKy2N7MUH6I6zX5myb4KwGvzuQtuTpyKO8vP+eZk/GRLFuZiGoQ8iprR0rBfGHLxKvISvfA+PqnxIB+KQ02tlGWIgMJTVweb4wWqfs1kGcJi1X8JDhyxN5clOjcLbF/F+lJVtBceCPsa5dTJPYA6cCUoHkScbkUHUp/SvA8oqTY0hQbehShB95mJrbjNBt2GlCxofoWMcOeU1bojkE8+THOLLROzo2W2BXlW7CceC6GrCKxSYoHo7IlnW7ECkGWO5/Pi6ZEmNgnZV/FmSCFjQDBSMtGx5LCdvR1KK+hGQoJaBU76u0kmrs8UXyeMUzxpPWFLp+0Wwo8hteBqEVLFLdLCERtNWDa0z9Yr9nuE4K79SEmvnuvDtQM0OkxRE+/HkTP4/GzX4wn42cvn0s1GaVQeoqQbzBFwtiUGnr+7PhF0vzTw6Of5R2Z2sg3wCw8mHvnbnhv7i286O6I/XerNFgQAvINqryl1J8v7HNXhhMZLIhf4R8F/aci4hz6UwYLZTxfFiDg9Be/f5eWBgg4/cXrQpSUUm91TZSUMm00jpLSboShEkoKwSzZAaWs5fvfEyglH7EZu7HC3y3JmlLXyx1UCsvFP8Aycqn1QqqvjJdSZIkkmnPA6xUwrsLOVBToEpApLdyJyvFvoZ3xjk9vb24SMoW/V7mbm/9ywBRheggNXR7RbU7utgKmKMJpXVa9vXlGuF8+rnqTqCklmbOtqCmZzCl7gzMZ8f1qMq+FTKks8VGauil53xRgyvYIfCSnb0zc6TmZ8pHYxKjeAGbK9kh6ea40J+fEi9WrKOc6wJTKcl4BMKU5Od8MXMr2yHkNuJRryznVU0sL+YawUrZHyGtgpVxbyNUwbYPTXk6BF+gqNRT4CugqTQk63SxcgwKPEDy2R85rYas0sKJXDNZOjpz21qLA12POtsKrNCDzOGa7UOZhCKdAY6kh8xXQWJqSeZq0BplHiB/bJPM1sFgakPmK4drJqw/WIvP1mLOtcCzXlnkUs10s8JImT6WllrgHaermNHl6xmztYCzbI+2BnL4xWa8Yrv3U2ggYy/aIeXmuNLmws3IVgrVvSG3tgrV3wdpJb+2CtdNQhnrVFgdrg5MbNALhNLhY7SK10xkmb4T1y0dq6yvKH1/9Yr7rq80fTrWrzR9O/TVHao9x0PQeX8nTHP9lgc2feCizEk3ytwhlZuHDco7H+DGgikxlgAhd2PLljILRSmVESJ9c2S52eUfRjqJPiCIuxFQGq8flljl3WSkut/wZ1lSL1Aa/9q8XlxsrE861SS1DWp/F5YYFcblcK65zVaxVIpK3Xz2SF1erKh8wWhcu73+CX1jRKoo2BUehURwwVCqaUW+wloV0D7CmoqjgNYflKgpGjaBbkINMFoCNkfshN+5WiZnF+kojEbE5Go1egRlOYDX0VulUgfkXbsSSVROukoxAqi64Mwk0TUrAnJH2lxw4Kqs7iY/K7CU1upoafdhqA2GitMyobTUXKIqmpKIwUbYGCf4J95jDme6kj2HQp+z/SypMgz4jOadwY3akIsJlSLLSMctc4Nx9Ks4Nd1l6Pz9LxH9KpwM0AZRX33PquJsZhWJKEyPYSCg6vGzyeuUD2MJN+kYf05l4fH2eV+xp8C3ZxAn9yj9M2qYhtPRpGtUojBrhZpU2HqR+CbJ6Xw5GE8Lofy43mfQW3yFhC0RKAr8zHpLgpiTMtE1wQn4tzxAJgrSIJZ0slnRyWELHVhrXKpz5vBUU2SoC+loJ9cx/JfaOxD6ApY9sZWL/SuwSRPKXDqg8O36gZuAoTUkDR+lPKXCUsyH1+ItDN0/EPofYM6iAwCttz6D+eCU647qBo0PedXmBo8mAiDh1YjNIlJY7ns+RZYJGVRZWDxpV67hm0Cgfkplho2jC/kKXT9q3gWGj5aJEx5Y4wsk+dTRqoH4Y4D9eAoeKlQ3tfPb06bNXj8bHFSsqDOwsE7p2+NB4fjGZe9ODWeC5vpMVJIjV1oJNK6DLw22kcNAA2dSLqydV3R8palAN4FyBLonO3MA1PHK3fW4sZ2/xe1rPdyCWs7d4HbaqkXG0NDw/cgPfjYwHsT04jbylT9r/Uq7nILyYhNPAm7gBjJ6tEDz7qAGGiCDTx8v5fPk+pqZuuGmZ1v6CcNMyZO3CTTfxfRduSj+7cFNOhtbC24Wbchp24aYtnt5N04U1sRVn2Xbhprtw01246S7cdBduugs33YWb7sJNryXnVE8tLeS7cNMNCPku3LQZBX4XboqG1S7ctGHm7MJNd+Gmu3DTXbhpPZnfhZvuwk134aacK7twU5ZxF266CzfdhZv+ZXcDgyFNj9bP6CGFXcgp/9rLHWW98iGn+oryx1ivmPf6avOHVO1q84dUbxdyOrZ2IacSd3YhpyxHEyGn9La7vlRmF3K6o2hH0adOERdiKoPVQ07LHIqsFHJa/kRrqklq4zp71ws5jZWJjCwVSC1DWq/cVbCpXlzn3iOrRNBpr4Gg07yoUkU1ybs+dh1ho3mRoG8RqWgBTX0TSQLWupAu8gUu/Snc94qJqnxf66cYl4oiJqnPJNVylI5lbZjyFLttl6kmkaRbGY2KDvhbyN4BKn8IlGv1jLKT8jsjdol5tYWrPmmKR5BSSkQk6J9yQ8LzqXjgrWQD0ORZu5wmEW3ax2Wk08U4rFHryQTHits8v/DYdlhKhIuxmC5BuhL0yrpGjnIUI1pyh1rS4XTyUe//qwl6AKSZ+x6xh+QgvKmrrZS/wbcXrvEN9eAAej9z/ciLrk4857NvPtv7vXVn9Pr2V5+FWNUpGyxEeghbkXUXNjFS+Sdwo5R17BP3yipWEPLWQKXMzPMdez7X1OVHcW/AtW/PQlIZ4YS555+Oo9wsnsNIB4kr+9Ste6H2ECgWv8pvwm1PdWLWT8iJESomL6R0JxNn5oyFP4BWOGMdyr+uOWMhce5klVOb6GZl5XtD2bcmq5Ups5mlzBdgiGnuC90FO32q30NLbIND7rUXL1eOHcVmyzTwVhGx7PijzkKZgU+9yFhdzOfGMvBOPd9Y2GHkBjkzcDed7/EM3F2UMUtaWJmsMEND+BgwuIsns7KzG3hx14KzmxJQppvdoLIYpN+JHIMl/ORkYXv+ycney/xOUa0SaHVggwIKPknAnkvkHZ+jxw5aduAScxa4tkNWnnswF2r31I3IzuAY+5tRdWwzcO5NIrx6LC7mkbcKlmSDM25uf7VczhW9n68lIuG5kvKLkvKjkvKzkvKDkvJSSXmmsHRxdTJdzpeB0CjFa54tvalLRhiWgKGyxgMt5nCxiqt7FATLAEnHXVQOjprAfXvhhlG4715O3RUJhA515jOUAYXswJ0vbSeyxGmFRBbcyHFndswg158u6WCYYGpMVODkzPaduXsSLCfLKCQtgZ54bM9DV9eQKOfOAjc8UwqeEJ1VGTw/vnjxfMxKPGdDiDAFCJLtOGfxSI4nPLT/P8bUK93ygsqAMh4ihbiQBDarbgHsNUBOjBv4MZRwOBGCSVJR9SbxHK2IJhPhUBm9Ezc4s0NvrvggdF4KtIMCPSNgl34MjmmMYUVwJvoG/IL4ZQ/Br/8gcoZ4D2uI32CIvSSjFk7AsjnC4jLFU+uojXPg2XiEJ18HVzrEZssQ1wGVbmWd0qwsxOiKVxY5kXxqrYtK9d8tls7F3CW2jonKjtASaTN/Rqrk92v8lbwq2EgQ/htWP/ab6J6iPNhNn/yVl2/uZ+EludelDfIwSunyljzxtc/JFBGxfPFUzyal5C1r9Q5roWORk4psHuT/+qyd/6EJfSu6Tb+MRM5++u+Mn6ocatKkfE4n6/mUtjs1k9p9K/WxDeS/X3711f8H2dhrtA==")))