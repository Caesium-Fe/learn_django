"""
fail逻辑
要用failed_unit_list： 所有fail了的sn坐标
判断是否有apple pass列
是：
    # 取出所有 "List of Apple Passing Tests" 列数据
    # 遍历"List of Apple Passing Tests" 列数据 为 下标和值
    #     判断 值为空 或者 值为NA
    #     是：
    #         continue
    #     判断 下标的sn的状态是否为 fail
    #     是：
    #         continue
    #     下标的sn的状态改为 apass
    #     apple_pass_unit_amount += 1

     遍历 failed_unit_list 为 sn 下标
        per_fail_item_list 为 list of failing test
        per_apple_item_list 为 List of Apple Passing Tests
        判断 per_fail_item_list 个数：
        没有：
            判断 per_apple_item_list 个数：
            没有：
                pass
            一个：
                dict[apple_fail_item] += 1
            否则：
                遍历 per_apple_item_list 为 apple_fail_item：
                    dict[apple_fail_item] += 1
        一个：
            判断 passforall 不在 per_fail_item_list中
            是：
                dict[fail—item] += 1
            判断 per_apple_item_list 个数：
            没有：
                pass
            一个：
                判断 是per_apple_item_list == ’NA‘
                是：
                    continue
                判断 是per_apple_item_list != per_fail_item_list
                是：
                    dict[apple_fail_item] += 1
            否则：
                遍历 per_apple_item_list 为 apple_fail_item：
                    判断 apple_fail_item != per_fail_item_list
                    是：
                        dict[apple_fail_item] += 1
        否则：
            遍历 per_fail_item_list 为 fail_item：
                判断 passforall 不在 fail——item中
                是：
                    dict[fail—item] += 1

            判断 per_apple_item_list 个数：
            没有：
                pass
            一个：
                判断 是per_apple_item_list == ’NA‘
                是：
                    continue
                判断 是per_apple_item_list 不在 per_fail_item_list
                是：
                    dict[apple_fail_item] += 1
            否则：
                遍历 per_apple_item_list 为 apple_fail_item：
                    判断 apple_fail_item 不在 per_fail_item_list
                    是：
                        dict[apple_fail_item] += 1
        得到error的description

    遍历 dict[apple_fail_item] 字典
        判断 apple_fail_item 在 dict[fail—item] 键中
        是：
            dict[fail_item] += dict[apple_fail_item]
        否：
            dict[fail_item] 里添加上这个 dict[apple_fail_item]


否：
	判断是否为pdca数据
	是：
		循环遍历failed_unit_list 为 sn坐标
		   取出每个sn的failing test list值 复制
            判断值的数量
            没有：
                pass
            一个：
                是否按照 if_item
                是：
                    这个fail值是否在所有数据的item中
                    是：
                        拿出这个item的limit2值, sn中属于这个item的值， sn的所有item值
                        判断 isfail 并且 是否apple——pass
                        是：
                        	判断是否这个sn的状态是否为fail
                        	是：
                        		判断是否 empty_fail 并且 所有item值中有空值
                        		是：
                        			dict[fail—item] += 1
                        		否：
                        			判断 check——empty——applepass
                        			是：
                        				applepass
                        			否：
                        				dict[fail—item] += 1
                     	否：
                     		dict[fail—item] += 1
				否：
					判断是否 apple_pass 并且 cof+fail_item 是否在 cof_data中
					是：
						判断check——empty——applepass
						是：
							applepass
						否：
							dict[fail—item] += 1
					否：
						dict[fail—item] += 1
			多个：
			    falling tests 被复制一遍 成为 unit_fail_item_list
				判断是否 if——item：
				是：
					遍历所有unit_fail_item_list 为 fail item
						拿出所有sn的item值
						判断 不是 apple pass 或者 （ empty_fail 并且 所有item值中有空）
						是：
						    is_unit_apple_pass = False
						    判断是 fail item在 所有item中：
						    是：
							    dict[fail—item] += 1
						若是 fail item在 所有item中：
							判断是 isfail 或 （empty 并且 所有item值中有空） 或 不是 check empty applepass
							是：
							    is_unit_apple_pass = False
								dict[fail—item] += 1
						否则：
							applepass
				否：
				    failing test items 复制成 per fail item
				    遍历所有per fail item 为 fail item
				        判断 不是 apple——pass
				        是：
				            is_unit_apple_pass = False
				            dict[fail—item] += 1
				        若是 cof+fail item 在 cof数据中 并且 cof+fail item 在per fail item中
				            is_unit_apple_pass = False
				            failing test items移除 cof+fail item
				            per fail item移除 cof+fail item
				            dict[fail—item] += 1
				        若是 cof+fail item 在 cof数据中 并且 cof+fail item 不在per fail item中
				            判断 fail——item是否为 cof开头
				            是：
				                is_unit_apple_pass = False
				                continue
				            判断 不是 check empty applepass
				            是：
				                is_unit_apple_pass = False
				                dict[fail—item] += 1
				            per fail item移除fail item
				        否则：
				            is_unit_apple_pass = False
				            判断 fail——item是否为 cof开头
				            是：
				                continue
				            dict[fail—item] += 1

				判断 是is_unit_apple_pass 并且 sn的状态为Fail 并且 len(unit_fail_item_list) != List of Failing Test len
                是：
                    applepass

            得到error的description 需要的参数 all_sn_data： "error description" 在数据中，则直接返回值，如果没有但是是pdca数据 则为None， 如果不是pdca 则报错。
            判断是否有 "error description" ：
                取 sn 数据的 "error description"
                判断 是有值
                是：
                    dict[unit_fail_error] += 1


	否：
	    循环遍历failed unit list 为 sn坐标
	        判断 list of failing tests数量
	        没有：
	            pass
            一个：
                判断 passforall 不在 list of failing test中：
                是：
                    dict[fail—item] += 1
            多个：
                遍历所有list of failing tests 为 单个 fail item
                    判断 passforall 不在 fail item中：
                    是：
                        dict[fail—item] += 1
            得到error的description： "error description" 在数据中，则直接返回值，如果没有但是是pdca数据 则为None， 如果不是pdca 则报错。
            判断是否有 "error description" ：
                取 sn 数据的 "error description"
                判断 是有值
                是：
                    dict[unit_fail_error] += 1

dict[fail—item] 拼接上 dict[unit_fail_error]

"""