(set-logic SLIA)
(synth-fun f ((name String)) String
    ((Start String (ntString))
     (ntString String (
           name
           " " "+" "-" "."
(str.++ ntString ntString)
(str.replace ntString ntString ntString)
(str.at ntString ntInt)
(int.to.str ntInt)
(ite ntBool ntString ntString)
(str.substr ntString ntInt ntInt)
))
      (ntInt Int (

            0 1 2 3 4 5
(+ ntInt ntInt)
(- ntInt ntInt)
(str.len ntString)
(str.to.int ntString)
(str.indexof ntString ntString ntInt)
))
(ntBool Bool (

      true false
(= ntInt ntInt)
(str.prefixof ntString ntString)
(str.suffixof ntString ntString)
(str.contains ntString ntString)
))
))
(constraint (= (f "+106 769-858-438") "106.769.858.438"))
(constraint (= (f "+106 769-858-438") "106.769.858.438"))
(constraint (= (f "+106 769-858-438") "106.769.858.438"))
(constraint (= (f "+83 973-757-831") "83.973.757.831"))
(constraint (= (f "+83 973-757-831") "83.973.757.831"))
(constraint (= (f "+83 973-757-831") "83.973.757.831"))
(constraint (= (f "+62 647-787-775") "62.647.787.775"))
(constraint (= (f "+62 647-787-775") "62.647.787.775"))
(constraint (= (f "+62 647-787-775") "62.647.787.775"))
(constraint (= (f "+172 027-507-632") "172.027.507.632"))
(constraint (= (f "+172 027-507-632") "172.027.507.632"))
(constraint (= (f "+172 027-507-632") "172.027.507.632"))
(constraint (= (f "+72 001-050-856") "72.001.050.856"))
(constraint (= (f "+72 001-050-856") "72.001.050.856"))
(constraint (= (f "+72 001-050-856") "72.001.050.856"))
(constraint (= (f "+95 310-537-401") "95.310.537.401"))
(constraint (= (f "+95 310-537-401") "95.310.537.401"))
(constraint (= (f "+95 310-537-401") "95.310.537.401"))
(constraint (= (f "+6 775-969-238") "6.775.969.238"))
(constraint (= (f "+6 775-969-238") "6.775.969.238"))
(constraint (= (f "+6 775-969-238") "6.775.969.238"))
(constraint (= (f "+174 594-539-946") "174.594.539.946"))
(constraint (= (f "+174 594-539-946") "174.594.539.946"))
(constraint (= (f "+174 594-539-946") "174.594.539.946"))
(constraint (= (f "+155 927-275-860") "155.927.275.860"))
(constraint (= (f "+155 927-275-860") "155.927.275.860"))
(constraint (= (f "+155 927-275-860") "155.927.275.860"))
(constraint (= (f "+167 405-461-331") "167.405.461.331"))
(constraint (= (f "+167 405-461-331") "167.405.461.331"))
(constraint (= (f "+167 405-461-331") "167.405.461.331"))
(constraint (= (f "+10 538-347-401") "10.538.347.401"))
(constraint (= (f "+10 538-347-401") "10.538.347.401"))
(constraint (= (f "+10 538-347-401") "10.538.347.401"))
(constraint (= (f "+60 971-986-103") "60.971.986.103"))
(constraint (= (f "+60 971-986-103") "60.971.986.103"))
(constraint (= (f "+60 971-986-103") "60.971.986.103"))
(constraint (= (f "+13 258-276-941") "13.258.276.941"))
(constraint (= (f "+13 258-276-941") "13.258.276.941"))
(constraint (= (f "+13 258-276-941") "13.258.276.941"))
(constraint (= (f "+2 604-746-137") "2.604.746.137"))
(constraint (= (f "+2 604-746-137") "2.604.746.137"))
(constraint (= (f "+2 604-746-137") "2.604.746.137"))
(constraint (= (f "+25 998-898-180") "25.998.898.180"))
(constraint (= (f "+25 998-898-180") "25.998.898.180"))
(constraint (= (f "+25 998-898-180") "25.998.898.180"))
(constraint (= (f "+151 862-946-541") "151.862.946.541"))
(constraint (= (f "+151 862-946-541") "151.862.946.541"))
(constraint (= (f "+151 862-946-541") "151.862.946.541"))
(constraint (= (f "+118 165-041-038") "118.165.041.038"))
(constraint (= (f "+118 165-041-038") "118.165.041.038"))
(constraint (= (f "+118 165-041-038") "118.165.041.038"))
(constraint (= (f "+144 170-592-272") "144.170.592.272"))
(constraint (= (f "+144 170-592-272") "144.170.592.272"))
(constraint (= (f "+144 170-592-272") "144.170.592.272"))
(constraint (= (f "+94 462-008-482") "94.462.008.482"))
(constraint (= (f "+94 462-008-482") "94.462.008.482"))
(constraint (= (f "+94 462-008-482") "94.462.008.482"))
(constraint (= (f "+82 685-122-086") "82.685.122.086"))
(constraint (= (f "+82 685-122-086") "82.685.122.086"))
(constraint (= (f "+82 685-122-086") "82.685.122.086"))
(constraint (= (f "+82 675-366-472") "82.675.366.472"))
(constraint (= (f "+82 675-366-472") "82.675.366.472"))
(constraint (= (f "+82 675-366-472") "82.675.366.472"))
(constraint (= (f "+80 066-433-096") "80.066.433.096"))
(constraint (= (f "+80 066-433-096") "80.066.433.096"))
(constraint (= (f "+80 066-433-096") "80.066.433.096"))
(constraint (= (f "+163 039-436-166") "163.039.436.166"))
(constraint (= (f "+163 039-436-166") "163.039.436.166"))
(constraint (= (f "+163 039-436-166") "163.039.436.166"))
(constraint (= (f "+138 808-083-074") "138.808.083.074"))
(constraint (= (f "+138 808-083-074") "138.808.083.074"))
(constraint (= (f "+138 808-083-074") "138.808.083.074"))
(constraint (= (f "+42 643-245-738") "42.643.245.738"))
(constraint (= (f "+42 643-245-738") "42.643.245.738"))
(constraint (= (f "+42 643-245-738") "42.643.245.738"))
(constraint (= (f "+169 822-542-726") "169.822.542.726"))
(constraint (= (f "+169 822-542-726") "169.822.542.726"))
(constraint (= (f "+169 822-542-726") "169.822.542.726"))
(constraint (= (f "+176 767-782-369") "176.767.782.369"))
(constraint (= (f "+176 767-782-369") "176.767.782.369"))
(constraint (= (f "+176 767-782-369") "176.767.782.369"))
(constraint (= (f "+47 414-369-343") "47.414.369.343"))
(constraint (= (f "+47 414-369-343") "47.414.369.343"))
(constraint (= (f "+47 414-369-343") "47.414.369.343"))
(constraint (= (f "+138 885-618-512") "138.885.618.512"))
(constraint (= (f "+138 885-618-512") "138.885.618.512"))
(constraint (= (f "+138 885-618-512") "138.885.618.512"))
(constraint (= (f "+104 158-671-355") "104.158.671.355"))
(constraint (= (f "+104 158-671-355") "104.158.671.355"))
(constraint (= (f "+104 158-671-355") "104.158.671.355"))
(constraint (= (f "+188 280-087-526") "188.280.087.526"))
(constraint (= (f "+188 280-087-526") "188.280.087.526"))
(constraint (= (f "+188 280-087-526") "188.280.087.526"))
(constraint (= (f "+50 268-571-336") "50.268.571.336"))
(constraint (= (f "+50 268-571-336") "50.268.571.336"))
(constraint (= (f "+50 268-571-336") "50.268.571.336"))
(constraint (= (f "+183 225-960-024") "183.225.960.024"))
(constraint (= (f "+183 225-960-024") "183.225.960.024"))
(constraint (= (f "+183 225-960-024") "183.225.960.024"))
(constraint (= (f "+58 191-982-491") "58.191.982.491"))
(constraint (= (f "+58 191-982-491") "58.191.982.491"))
(constraint (= (f "+58 191-982-491") "58.191.982.491"))
(constraint (= (f "+9 507-092-535") "9.507.092.535"))
(constraint (= (f "+9 507-092-535") "9.507.092.535"))
(constraint (= (f "+9 507-092-535") "9.507.092.535"))
(constraint (= (f "+64 061-601-398") "64.061.601.398"))
(constraint (= (f "+64 061-601-398") "64.061.601.398"))
(constraint (= (f "+64 061-601-398") "64.061.601.398"))
(constraint (= (f "+189 831-591-877") "189.831.591.877"))
(constraint (= (f "+189 831-591-877") "189.831.591.877"))
(constraint (= (f "+189 831-591-877") "189.831.591.877"))
(constraint (= (f "+129 425-765-844") "129.425.765.844"))
(constraint (= (f "+129 425-765-844") "129.425.765.844"))
(constraint (= (f "+129 425-765-844") "129.425.765.844"))
(constraint (= (f "+94 856-734-046") "94.856.734.046"))
(constraint (= (f "+94 856-734-046") "94.856.734.046"))
(constraint (= (f "+94 856-734-046") "94.856.734.046"))
(constraint (= (f "+35 082-845-261") "35.082.845.261"))
(constraint (= (f "+35 082-845-261") "35.082.845.261"))
(constraint (= (f "+35 082-845-261") "35.082.845.261"))
(constraint (= (f "+185 394-622-272") "185.394.622.272"))
(constraint (= (f "+185 394-622-272") "185.394.622.272"))
(constraint (= (f "+185 394-622-272") "185.394.622.272"))
(constraint (= (f "+163 905-707-740") "163.905.707.740"))
(constraint (= (f "+163 905-707-740") "163.905.707.740"))
(constraint (= (f "+163 905-707-740") "163.905.707.740"))
(constraint (= (f "+23 448-213-807") "23.448.213.807"))
(constraint (= (f "+23 448-213-807") "23.448.213.807"))
(constraint (= (f "+23 448-213-807") "23.448.213.807"))
(constraint (= (f "+42 634-077-089") "42.634.077.089"))
(constraint (= (f "+42 634-077-089") "42.634.077.089"))
(constraint (= (f "+42 634-077-089") "42.634.077.089"))
(constraint (= (f "+18 051-287-382") "18.051.287.382"))
(constraint (= (f "+18 051-287-382") "18.051.287.382"))
(constraint (= (f "+18 051-287-382") "18.051.287.382"))
(constraint (= (f "+29 773-545-520") "29.773.545.520"))
(constraint (= (f "+29 773-545-520") "29.773.545.520"))
(constraint (= (f "+29 773-545-520") "29.773.545.520"))
(constraint (= (f "+43 249-097-743") "43.249.097.743"))
(constraint (= (f "+43 249-097-743") "43.249.097.743"))
(constraint (= (f "+43 249-097-743") "43.249.097.743"))
(constraint (= (f "+158 674-736-891") "158.674.736.891"))
(constraint (= (f "+158 674-736-891") "158.674.736.891"))
(constraint (= (f "+158 674-736-891") "158.674.736.891"))
(constraint (= (f "+45 124-771-454") "45.124.771.454"))
(constraint (= (f "+45 124-771-454") "45.124.771.454"))
(constraint (= (f "+45 124-771-454") "45.124.771.454"))
(constraint (= (f "+180 029-457-654") "180.029.457.654"))
(constraint (= (f "+180 029-457-654") "180.029.457.654"))
(constraint (= (f "+180 029-457-654") "180.029.457.654"))
(constraint (= (f "+75 227-250-652") "75.227.250.652"))
(constraint (= (f "+75 227-250-652") "75.227.250.652"))
(constraint (= (f "+75 227-250-652") "75.227.250.652"))
(constraint (= (f "+5 528-317-854") "5.528.317.854"))
(constraint (= (f "+5 528-317-854") "5.528.317.854"))
(constraint (= (f "+5 528-317-854") "5.528.317.854"))
(constraint (= (f "+81 849-629-290") "81.849.629.290"))
(constraint (= (f "+81 849-629-290") "81.849.629.290"))
(constraint (= (f "+81 849-629-290") "81.849.629.290"))
(constraint (= (f "+46 005-119-176") "46.005.119.176"))
(constraint (= (f "+46 005-119-176") "46.005.119.176"))
(constraint (= (f "+46 005-119-176") "46.005.119.176"))
(constraint (= (f "+108 150-380-705") "108.150.380.705"))
(constraint (= (f "+108 150-380-705") "108.150.380.705"))
(constraint (= (f "+108 150-380-705") "108.150.380.705"))
(constraint (= (f "+40 122-224-247") "40.122.224.247"))
(constraint (= (f "+40 122-224-247") "40.122.224.247"))
(constraint (= (f "+40 122-224-247") "40.122.224.247"))
(constraint (= (f "+68 890-680-027") "68.890.680.027"))
(constraint (= (f "+68 890-680-027") "68.890.680.027"))
(constraint (= (f "+68 890-680-027") "68.890.680.027"))
(constraint (= (f "+169 060-204-504") "169.060.204.504"))
(constraint (= (f "+169 060-204-504") "169.060.204.504"))
(constraint (= (f "+169 060-204-504") "169.060.204.504"))
(constraint (= (f "+95 620-820-945") "95.620.820.945"))
(constraint (= (f "+95 620-820-945") "95.620.820.945"))
(constraint (= (f "+95 620-820-945") "95.620.820.945"))
(constraint (= (f "+43 592-938-846") "43.592.938.846"))
(constraint (= (f "+43 592-938-846") "43.592.938.846"))
(constraint (= (f "+43 592-938-846") "43.592.938.846"))
(constraint (= (f "+7 023-296-647") "7.023.296.647"))
(constraint (= (f "+7 023-296-647") "7.023.296.647"))
(constraint (= (f "+7 023-296-647") "7.023.296.647"))
(constraint (= (f "+20 541-401-396") "20.541.401.396"))
(constraint (= (f "+20 541-401-396") "20.541.401.396"))
(constraint (= (f "+20 541-401-396") "20.541.401.396"))
(constraint (= (f "+64 751-365-934") "64.751.365.934"))
(constraint (= (f "+64 751-365-934") "64.751.365.934"))
(constraint (= (f "+64 751-365-934") "64.751.365.934"))
(constraint (= (f "+163 546-119-476") "163.546.119.476"))
(constraint (= (f "+163 546-119-476") "163.546.119.476"))
(constraint (= (f "+163 546-119-476") "163.546.119.476"))
(constraint (= (f "+198 557-666-779") "198.557.666.779"))
(constraint (= (f "+198 557-666-779") "198.557.666.779"))
(constraint (= (f "+198 557-666-779") "198.557.666.779"))
(constraint (= (f "+14 673-759-017") "14.673.759.017"))
(constraint (= (f "+14 673-759-017") "14.673.759.017"))
(constraint (= (f "+14 673-759-017") "14.673.759.017"))
(constraint (= (f "+161 086-020-168") "161.086.020.168"))
(constraint (= (f "+161 086-020-168") "161.086.020.168"))
(constraint (= (f "+161 086-020-168") "161.086.020.168"))
(constraint (= (f "+65 970-575-488") "65.970.575.488"))
(constraint (= (f "+65 970-575-488") "65.970.575.488"))
(constraint (= (f "+65 970-575-488") "65.970.575.488"))
(constraint (= (f "+2 455-126-377") "2.455.126.377"))
(constraint (= (f "+2 455-126-377") "2.455.126.377"))
(constraint (= (f "+2 455-126-377") "2.455.126.377"))
(constraint (= (f "+196 728-585-376") "196.728.585.376"))
(constraint (= (f "+196 728-585-376") "196.728.585.376"))
(constraint (= (f "+196 728-585-376") "196.728.585.376"))
(constraint (= (f "+33 117-430-125") "33.117.430.125"))
(constraint (= (f "+33 117-430-125") "33.117.430.125"))
(constraint (= (f "+33 117-430-125") "33.117.430.125"))
(constraint (= (f "+195 488-831-768") "195.488.831.768"))
(constraint (= (f "+195 488-831-768") "195.488.831.768"))
(constraint (= (f "+195 488-831-768") "195.488.831.768"))
(constraint (= (f "+86 468-718-108") "86.468.718.108"))
(constraint (= (f "+86 468-718-108") "86.468.718.108"))
(constraint (= (f "+86 468-718-108") "86.468.718.108"))
(constraint (= (f "+194 278-716-950") "194.278.716.950"))
(constraint (= (f "+194 278-716-950") "194.278.716.950"))
(constraint (= (f "+194 278-716-950") "194.278.716.950"))
(constraint (= (f "+43 730-685-847") "43.730.685.847"))
(constraint (= (f "+43 730-685-847") "43.730.685.847"))
(constraint (= (f "+43 730-685-847") "43.730.685.847"))
(constraint (= (f "+140 794-289-551") "140.794.289.551"))
(constraint (= (f "+140 794-289-551") "140.794.289.551"))
(constraint (= (f "+140 794-289-551") "140.794.289.551"))
(constraint (= (f "+21 679-740-834") "21.679.740.834"))
(constraint (= (f "+21 679-740-834") "21.679.740.834"))
(constraint (= (f "+21 679-740-834") "21.679.740.834"))
(constraint (= (f "+98 717-997-323") "98.717.997.323"))
(constraint (= (f "+98 717-997-323") "98.717.997.323"))
(constraint (= (f "+98 717-997-323") "98.717.997.323"))
(constraint (= (f "+47 401-100-231") "47.401.100.231"))
(constraint (= (f "+47 401-100-231") "47.401.100.231"))
(constraint (= (f "+47 401-100-231") "47.401.100.231"))
(constraint (= (f "+143 726-462-368") "143.726.462.368"))
(constraint (= (f "+143 726-462-368") "143.726.462.368"))
(constraint (= (f "+143 726-462-368") "143.726.462.368"))
(constraint (= (f "+147 864-005-968") "147.864.005.968"))
(constraint (= (f "+147 864-005-968") "147.864.005.968"))
(constraint (= (f "+147 864-005-968") "147.864.005.968"))
(constraint (= (f "+130 590-757-665") "130.590.757.665"))
(constraint (= (f "+130 590-757-665") "130.590.757.665"))
(constraint (= (f "+130 590-757-665") "130.590.757.665"))
(constraint (= (f "+197 700-858-976") "197.700.858.976"))
(constraint (= (f "+197 700-858-976") "197.700.858.976"))
(constraint (= (f "+197 700-858-976") "197.700.858.976"))
(constraint (= (f "+158 344-541-946") "158.344.541.946"))
(constraint (= (f "+158 344-541-946") "158.344.541.946"))
(constraint (= (f "+158 344-541-946") "158.344.541.946"))
(constraint (= (f "+56 242-901-234") "56.242.901.234"))
(constraint (= (f "+56 242-901-234") "56.242.901.234"))
(constraint (= (f "+56 242-901-234") "56.242.901.234"))
(constraint (= (f "+132 313-075-754") "132.313.075.754"))
(constraint (= (f "+132 313-075-754") "132.313.075.754"))
(constraint (= (f "+132 313-075-754") "132.313.075.754"))
(constraint (= (f "+130 517-953-149") "130.517.953.149"))
(constraint (= (f "+130 517-953-149") "130.517.953.149"))
(constraint (= (f "+130 517-953-149") "130.517.953.149"))
(constraint (= (f "+158 684-878-743") "158.684.878.743"))
(constraint (= (f "+158 684-878-743") "158.684.878.743"))
(constraint (= (f "+158 684-878-743") "158.684.878.743"))
(constraint (= (f "+52 836-582-035") "52.836.582.035"))
(constraint (= (f "+52 836-582-035") "52.836.582.035"))
(constraint (= (f "+52 836-582-035") "52.836.582.035"))
(constraint (= (f "+138 117-484-671") "138.117.484.671"))
(constraint (= (f "+138 117-484-671") "138.117.484.671"))
(constraint (= (f "+138 117-484-671") "138.117.484.671"))
(constraint (= (f "+50 012-148-873") "50.012.148.873"))
(constraint (= (f "+50 012-148-873") "50.012.148.873"))
(constraint (= (f "+50 012-148-873") "50.012.148.873"))
(constraint (= (f "+105 048-919-483") "105.048.919.483"))
(constraint (= (f "+105 048-919-483") "105.048.919.483"))
(constraint (= (f "+105 048-919-483") "105.048.919.483"))
(constraint (= (f "+18 209-851-997") "18.209.851.997"))
(constraint (= (f "+18 209-851-997") "18.209.851.997"))
(constraint (= (f "+18 209-851-997") "18.209.851.997"))
(constraint (= (f "+176 938-056-084") "176.938.056.084"))
(constraint (= (f "+176 938-056-084") "176.938.056.084"))
(constraint (= (f "+176 938-056-084") "176.938.056.084"))
(constraint (= (f "+141 018-132-973") "141.018.132.973"))
(constraint (= (f "+141 018-132-973") "141.018.132.973"))
(constraint (= (f "+141 018-132-973") "141.018.132.973"))
(constraint (= (f "+199 936-162-415") "199.936.162.415"))
(constraint (= (f "+199 936-162-415") "199.936.162.415"))
(constraint (= (f "+199 936-162-415") "199.936.162.415"))
(constraint (= (f "+33 547-051-264") "33.547.051.264"))
(constraint (= (f "+33 547-051-264") "33.547.051.264"))
(constraint (= (f "+33 547-051-264") "33.547.051.264"))
(constraint (= (f "+161 233-981-513") "161.233.981.513"))
(constraint (= (f "+161 233-981-513") "161.233.981.513"))
(constraint (= (f "+161 233-981-513") "161.233.981.513"))
(constraint (= (f "+115 101-728-328") "115.101.728.328"))
(constraint (= (f "+115 101-728-328") "115.101.728.328"))
(constraint (= (f "+115 101-728-328") "115.101.728.328"))
(constraint (= (f "+45 095-746-635") "45.095.746.635"))
(constraint (= (f "+45 095-746-635") "45.095.746.635"))
(constraint (= (f "+45 095-746-635") "45.095.746.635"))
(constraint (= (f "+106 769-858-438") "106.769.858.438"))
(constraint (= (f "+83 973-757-831") "83.973.757.831"))
(constraint (= (f "+62 647-787-775") "62.647.787.775"))
(constraint (= (f "+172 027-507-632") "172.027.507.632"))
(constraint (= (f "+72 001-050-856") "72.001.050.856"))
(constraint (= (f "+95 310-537-401") "95.310.537.401"))
(constraint (= (f "+6 775-969-238") "6.775.969.238"))
(constraint (= (f "+174 594-539-946") "174.594.539.946"))
(constraint (= (f "+155 927-275-860") "155.927.275.860"))
(constraint (= (f "+167 405-461-331") "167.405.461.331"))
(constraint (= (f "+10 538-347-401") "10.538.347.401"))
(constraint (= (f "+60 971-986-103") "60.971.986.103"))
(constraint (= (f "+13 258-276-941") "13.258.276.941"))
(constraint (= (f "+2 604-746-137") "2.604.746.137"))
(constraint (= (f "+25 998-898-180") "25.998.898.180"))
(constraint (= (f "+151 862-946-541") "151.862.946.541"))
(constraint (= (f "+118 165-041-038") "118.165.041.038"))
(constraint (= (f "+144 170-592-272") "144.170.592.272"))
(constraint (= (f "+94 462-008-482") "94.462.008.482"))
(constraint (= (f "+82 685-122-086") "82.685.122.086"))
(constraint (= (f "+82 675-366-472") "82.675.366.472"))
(constraint (= (f "+80 066-433-096") "80.066.433.096"))
(constraint (= (f "+163 039-436-166") "163.039.436.166"))
(constraint (= (f "+138 808-083-074") "138.808.083.074"))
(constraint (= (f "+42 643-245-738") "42.643.245.738"))
(constraint (= (f "+169 822-542-726") "169.822.542.726"))
(constraint (= (f "+176 767-782-369") "176.767.782.369"))
(constraint (= (f "+47 414-369-343") "47.414.369.343"))
(constraint (= (f "+138 885-618-512") "138.885.618.512"))
(constraint (= (f "+104 158-671-355") "104.158.671.355"))
(constraint (= (f "+188 280-087-526") "188.280.087.526"))
(constraint (= (f "+50 268-571-336") "50.268.571.336"))
(constraint (= (f "+183 225-960-024") "183.225.960.024"))
(constraint (= (f "+58 191-982-491") "58.191.982.491"))
(constraint (= (f "+9 507-092-535") "9.507.092.535"))
(constraint (= (f "+64 061-601-398") "64.061.601.398"))
(constraint (= (f "+189 831-591-877") "189.831.591.877"))
(constraint (= (f "+129 425-765-844") "129.425.765.844"))
(constraint (= (f "+94 856-734-046") "94.856.734.046"))
(constraint (= (f "+35 082-845-261") "35.082.845.261"))
(constraint (= (f "+185 394-622-272") "185.394.622.272"))
(constraint (= (f "+163 905-707-740") "163.905.707.740"))
(constraint (= (f "+23 448-213-807") "23.448.213.807"))
(constraint (= (f "+42 634-077-089") "42.634.077.089"))
(constraint (= (f "+18 051-287-382") "18.051.287.382"))
(constraint (= (f "+29 773-545-520") "29.773.545.520"))
(constraint (= (f "+43 249-097-743") "43.249.097.743"))
(constraint (= (f "+158 674-736-891") "158.674.736.891"))
(constraint (= (f "+45 124-771-454") "45.124.771.454"))
(constraint (= (f "+180 029-457-654") "180.029.457.654"))
(constraint (= (f "+75 227-250-652") "75.227.250.652"))
(constraint (= (f "+5 528-317-854") "5.528.317.854"))
(constraint (= (f "+81 849-629-290") "81.849.629.290"))
(constraint (= (f "+46 005-119-176") "46.005.119.176"))
(constraint (= (f "+108 150-380-705") "108.150.380.705"))
(constraint (= (f "+40 122-224-247") "40.122.224.247"))
(constraint (= (f "+68 890-680-027") "68.890.680.027"))
(constraint (= (f "+169 060-204-504") "169.060.204.504"))
(constraint (= (f "+95 620-820-945") "95.620.820.945"))
(constraint (= (f "+43 592-938-846") "43.592.938.846"))
(constraint (= (f "+7 023-296-647") "7.023.296.647"))
(constraint (= (f "+20 541-401-396") "20.541.401.396"))
(constraint (= (f "+64 751-365-934") "64.751.365.934"))
(constraint (= (f "+163 546-119-476") "163.546.119.476"))
(constraint (= (f "+198 557-666-779") "198.557.666.779"))
(constraint (= (f "+14 673-759-017") "14.673.759.017"))
(constraint (= (f "+161 086-020-168") "161.086.020.168"))
(constraint (= (f "+65 970-575-488") "65.970.575.488"))
(constraint (= (f "+2 455-126-377") "2.455.126.377"))
(constraint (= (f "+196 728-585-376") "196.728.585.376"))
(constraint (= (f "+33 117-430-125") "33.117.430.125"))
(constraint (= (f "+195 488-831-768") "195.488.831.768"))
(constraint (= (f "+86 468-718-108") "86.468.718.108"))
(constraint (= (f "+194 278-716-950") "194.278.716.950"))
(constraint (= (f "+43 730-685-847") "43.730.685.847"))
(constraint (= (f "+140 794-289-551") "140.794.289.551"))
(constraint (= (f "+21 679-740-834") "21.679.740.834"))
(constraint (= (f "+98 717-997-323") "98.717.997.323"))
(constraint (= (f "+47 401-100-231") "47.401.100.231"))
(constraint (= (f "+143 726-462-368") "143.726.462.368"))
(constraint (= (f "+147 864-005-968") "147.864.005.968"))
(constraint (= (f "+130 590-757-665") "130.590.757.665"))
(constraint (= (f "+197 700-858-976") "197.700.858.976"))
(constraint (= (f "+158 344-541-946") "158.344.541.946"))
(constraint (= (f "+56 242-901-234") "56.242.901.234"))
(constraint (= (f "+132 313-075-754") "132.313.075.754"))
(constraint (= (f "+130 517-953-149") "130.517.953.149"))
(constraint (= (f "+158 684-878-743") "158.684.878.743"))
(constraint (= (f "+52 836-582-035") "52.836.582.035"))
(constraint (= (f "+138 117-484-671") "138.117.484.671"))
(constraint (= (f "+50 012-148-873") "50.012.148.873"))
(constraint (= (f "+105 048-919-483") "105.048.919.483"))
(constraint (= (f "+18 209-851-997") "18.209.851.997"))
(constraint (= (f "+176 938-056-084") "176.938.056.084"))
(constraint (= (f "+141 018-132-973") "141.018.132.973"))
(constraint (= (f "+199 936-162-415") "199.936.162.415"))
(constraint (= (f "+33 547-051-264") "33.547.051.264"))
(constraint (= (f "+161 233-981-513") "161.233.981.513"))
(constraint (= (f "+115 101-728-328") "115.101.728.328"))
(constraint (= (f "+45 095-746-635") "45.095.746.635"))

(check-synth)
