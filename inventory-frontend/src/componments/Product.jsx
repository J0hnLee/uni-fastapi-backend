import React, { useEffect, useState } from "react";
import Wrapper from "./Wrapper";
export default function Product() {
  const [products, setProducts] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8000/products");
        const content = await response.json(); // 等待解析 JSON
        setProducts(content); // 將已解析的 JSON 設置為 products 狀態
        // console.log(products); // 在主控台打印 products
      } catch (error) {
        console.error("發生錯誤：", error);
      }
    };

    fetchData(); // 呼叫異步函數
  }, []);
  return (
    <Wrapper>
      <div class="table-responsive small">
        {/* {console.log(products)}
        <p>{products}</p> */}
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th scope="col">產品ID</th>
              <th scope="col">產品名稱</th>
              <th scope="col">產品價格</th>
              <th scope="col">產品數量</th>
              <th scope="col">刪除</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product) => {
              return (
                <tr key={product.id}>
                  <td>{product.id}</td>
                  <td>{product.name}</td>
                  <td>{product.price}</td>
                  <td>{product.quantity}</td>
                  <td>
                    <a href="#" className="btn btn-sm btn-outline-secondary">
                      Delete
                    </a>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </Wrapper>
  );
}
